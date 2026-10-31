import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/reference-search/scripts/cache.py'
spec = importlib.util.spec_from_file_location('reference_cache', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class CacheTests(unittest.TestCase):
    def test_composition_language_survives_resume_and_stays_project_local(self):
        language = {'id': 'composition-a', 'revision': 2, 'status': 'draft',
                    'principles': [{'rule': 'Keep form titles aligned with field labels'}],
                    'visual_anchors': [], 'history': [{'revision': 1, 'reason': 'Form adaptation'}]}
        identity = {'id': 'brand-a', 'bindings': {'background': 'variable-1'},
                    'composition_language': language}
        self.cache.plan_parts('design', {'identity': identity, 'parts': [
            {'id': 'home', 'title': 'Home', 'scope': 'Home screen'}]})
        resumed = module.Cache(self.a, self.shared)
        resumed.init()
        resumed.plan_parts('design', {'parts': [
            {'id': 'login', 'title': 'Login', 'scope': 'Login screen'}]})
        state = resumed.status()['state']
        self.assertEqual(state['identity'], identity)
        self.assertIn('home', state['tasks']['design']['parts'])
        self.assertIn('login', state['tasks']['design']['parts'])
        other = module.Cache(self.b, self.shared)
        other.init()
        self.assertNotIn('identity', other.status()['state'])
        self.assertNotIn('composition-a', (self.shared / 'catalog.json').read_text())

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='.cache-test-', dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.shared = self.base / 'shared'
        self.a = self.base / 'project-a'; self.a.mkdir()
        self.b = self.base / 'project-b'; self.b.mkdir()
        self.cache = module.Cache(self.a, self.shared)
        self.cache.init()
        self.asset = self.a / 'capture.svg'
        self.asset.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"/>')
        self.meta = {'title': 'Checkout mobile', 'source_url': 'https://example.com/checkout',
                     'source_kind': 'live-product', 'public_source': True, 'tags': ['checkout', 'mobile']}

    def test_reuse_across_projects_and_dedup(self):
        entry = self.cache.add(self.asset, self.meta, shared=True)
        self.assertEqual(self.cache.add(self.asset, self.meta, shared=True)['id'], entry['id'])
        other = module.Cache(self.b, self.shared); other.init()
        self.assertEqual(other.find('mobile checkout')[0]['scope'], 'shared')
        copy = other.reuse(entry['id'])
        self.assertEqual((self.b / copy['versions'][0]['asset_path']).read_bytes(), self.asset.read_bytes())
        other.reuse(entry['id'])
        self.assertEqual(other.status()['local_references'], 1)
        self.assertEqual(other.find('checkout')[0]['scope'], 'local')
        self.assertEqual(len(other.find('checkout')), 1)
        # Local copy survives shared-image loss.
        (self.shared / entry['versions'][0]['asset_path']).unlink()
        self.assertTrue((self.b / copy['versions'][0]['asset_path']).is_file())

    def test_private_capture_and_decisions_stay_local(self):
        private = {'title': 'Client upload', 'source_kind': 'user-upload'}
        with self.assertRaises(ValueError): self.cache.add(self.asset, private, shared=True)
        with self.assertRaises(ValueError): self.cache.add(self.asset, dict(self.meta, user_quote='Private choice'), shared=True)
        self.cache.add(self.asset, private)
        self.cache.checkpoint('task-a', {'status': 'waiting_for_user', 'waiting_for': 'choose card A', 'next_action': 'apply selected header'})
        other = module.Cache(self.b, self.shared); other.init()
        self.assertEqual(other.find('Client'), [])
        self.assertEqual(other.status()['state']['tasks'], {})
        self.assertNotIn('choose card A', (self.shared / 'catalog.json').read_text())

    def test_resume_preserves_pending_action_and_completed_tasks(self):
        self.cache.checkpoint('task-a', {'status': 'in_progress', 'last_confirmed': 'board inspected',
            'pending_action': {'operation_id': 'op-123'}, 'next_action': 'reconcile op-123'})
        module.Cache(self.a).init()
        task = module.Cache(self.a).status()['state']['tasks']['task-a']
        self.assertEqual(task['pending_action']['operation_id'], 'op-123')
        with self.assertRaises(ValueError): self.cache.checkpoint('task-a', {'status': 'complete'})
        self.cache.checkpoint('task-a', {'status': 'complete', 'pending_action': None})
        self.cache.checkpoint('task-b', {'status': 'in_progress'})
        self.assertEqual(self.cache.status()['state']['tasks']['task-a']['status'], 'complete')

    def test_hash_check_rejects_corruption(self):
        entry = self.cache.add(self.asset, self.meta, shared=True)
        (self.shared / entry['versions'][0]['asset_path']).write_text('corrupt')
        with self.assertRaises(ValueError): self.cache.reuse(entry['id'])
        self.assertEqual(self.cache.status()['local_references'], 0)

    def test_v1_migration_preserves_choices_and_unknown_fields(self):
        path = self.cache.local / 'references/catalog.json'
        old = {'schema_version': 1, 'references': [], 'selections': [{'id': 'sel-1', 'user_quote': 'A header'}], 'custom': True}
        path.write_text(json.dumps(old))
        self.cache.init()
        current = json.loads(path.read_text())
        self.assertEqual(current['selections'], old['selections'])
        self.assertTrue(current['custom'])
        self.assertEqual(json.loads(path.with_name('catalog.v1.backup.json').read_text()), old)

    def test_concurrent_shared_writes_do_not_lose_references(self):
        processes = []
        for i in range(4):
            meta = self.a / f'meta-{i}.json'
            meta.write_text(json.dumps(dict(self.meta, source_url=f'https://example.com/{i}')))
            processes.append(subprocess.Popen([sys.executable, '-B', str(SCRIPT), '--project', str(self.a),
                '--shared-root', str(self.shared), 'add', '--asset', str(self.asset), '--metadata', str(meta), '--shared'],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        for p in processes:
            out, err = p.communicate(timeout=15)
            self.assertEqual(p.returncode, 0, err)
        self.assertEqual(self.cache.status()['shared_references'], 4)

    def test_quality_is_versioned_and_separate_from_project_choice(self):
        entry = self.cache.add(self.asset, self.meta, shared=True)
        review = {'version_id': entry['versions'][0]['id'], 'verdict': 'mixed',
                  'scores': {'layout': 4, 'typography': 2}, 'strengths': ['Clear groups'],
                  'weaknesses': ['Small captions'], 'evidence': 'Inspected saved capture',
                  'inspected_at': '2026-10-31T10:00:00Z'}
        self.cache.review(entry['id'], review, shared=True)
        self.cache.review(entry['id'], review, shared=True)
        copy = self.cache.reuse(entry['id'])
        self.assertEqual(len(copy['quality_reviews']), 1)
        with self.assertRaises(ValueError):
            self.cache.review(entry['id'], dict(review, user_quote='I like A'), shared=True)
        with self.assertRaises(ValueError):
            self.cache.review(entry['id'], dict(review, scores={'layout': 6}), shared=True)
        with self.assertRaises(ValueError):
            self.cache.review(entry['id'], dict(review, version_id='wrong'), shared=True)

    def test_search_resume_dedup_and_new_filters(self):
        request = {'source': 'https://example.com/gallery', 'query': 'Mobile Checkout',
                   'filters': {'sort': 'popular'}, 'public_source': True}
        page = {'request_token': 'page-1', 'url': 'https://example.com/gallery?page=1',
                'pagination_mode': 'numbered', 'result_ids': ['ref-a'], 'next_token': 'page-2',
                'outcome': 'visited', 'observed_at': '2026-10-31T10:00:00Z'}
        self.cache.search_log(request, page, shared=True)
        self.cache.search_log(request, page, shared=True)
        other = module.Cache(self.b, self.shared); other.init()
        equivalent = dict(request, query='  mobile   CHECKOUT ')
        log = other.search_log(equivalent, shared=True)
        self.assertEqual(log['next_token'], 'page-2')
        self.assertEqual(len(log['pages']), 1)
        self.assertIsNone(other.search_log(dict(request, filters={'sort': 'recent'}), shared=True))
        page2 = dict(page, request_token='page-2', result_ids=['ref-a', 'ref-b'], next_token='page-3', coverage_satisfied=True)
        log = other.search_log(request, page2, shared=True)
        self.assertEqual(log['status'], 'covered')
        self.assertEqual(log['next_token'], 'page-3')
        self.assertEqual(log['result_ids'], ['ref-a', 'ref-b'])

    def test_pagination_loop_unknown_end_and_blocked_retry(self):
        request = {'source': 'https://example.com/gallery', 'query': 'cards'}
        page = {'request_token': 'batch-1', 'pagination_mode': 'infinite-scroll',
                'result_ids': [], 'next_token': 'batch-1', 'outcome': 'visited',
                'observed_at': '2026-10-31T10:00:00Z'}
        self.assertEqual(self.cache.search_log(request, page)['status'], 'paused')
        no_next = dict(page, request_token='batch-2', next_token=None)
        self.assertEqual(self.cache.search_log(request, no_next)['status'], 'paused')
        blocked = dict(page, request_token='batch-3', outcome='blocked', next_token=None, retry_after='later')
        log = self.cache.search_log(request, blocked)
        self.assertEqual(log['status'], 'blocked')
        self.assertEqual(log['next_token'], 'batch-3')
        ended = dict(no_next, request_token='batch-3', end_confirmed=True, reason='Visible end of results')
        self.assertEqual(self.cache.search_log(request, ended)['status'], 'exhausted')
        with self.assertRaises(ValueError): self.cache.search_log(request, page, shared=True)
        with self.assertRaises(ValueError): self.cache.search_log(request, dict(page, end_confirmed=True))

    def sample_plan(self):
        return {'identity': {'id': 'brand-1', 'status': 'unresolved'}, 'parts': [
            {'id': 'home', 'title': 'Home', 'scope': 'Compose home'},
            {'id': 'header', 'title': 'Header', 'scope': 'Navigation', 'parent_id': 'home'},
            {'id': 'products', 'title': 'Products', 'scope': 'Product cards', 'parent_id': 'home'},
            {'id': 'cart', 'title': 'Cart', 'scope': 'Shopping cart'}]}

    def test_parts_resume_one_identity_and_preserve_completed(self):
        plan = self.sample_plan()
        self.cache.plan_parts('design', plan)
        self.cache.part_checkpoint('design', 'header', {'status': 'complete', 'last_confirmed': 'Header verified'})
        self.cache.part_checkpoint('design', 'products', {'status': 'waiting_for_user', 'waiting_for': 'Choose cards', 'next_action': 'Apply choice'})
        self.cache.plan_parts('design', plan)
        resumed = module.Cache(self.a).status()['state']
        parts = resumed['tasks']['design']['parts']
        self.assertEqual(parts['header']['status'], 'complete')
        self.assertEqual(parts['products']['next_action'], 'Apply choice')
        self.assertEqual(resumed['tasks']['design']['identity_id'], resumed['identity']['id'])
        self.assertEqual(self.cache.ready_parts('design')['ready'], ['cart'])
        with self.assertRaises(ValueError):
            self.cache.plan_parts('design', dict(plan, identity={'id': 'different'}))
        with self.assertRaises(ValueError):
            self.cache.checkpoint('design', {'status': 'complete', 'integration_check': 'Verified shared identity and assembled screens'})
        with self.assertRaises(ValueError):
            self.cache.part_checkpoint('design', 'products', {'status': 'complete', 'last_confirmed': 'Claim'})

    def test_part_dependency_cycles_and_pending_writes(self):
        plan = self.sample_plan()
        plan['parts'][1]['depends_on'] = ['home']
        with self.assertRaises(ValueError): self.cache.plan_parts('bad', plan)
        self.assertNotIn('bad', self.cache.status()['state']['tasks'])
        self.cache.plan_parts('design', self.sample_plan())
        self.cache.part_checkpoint('design', 'header', {'status': 'in_progress', 'pending_action': {'operation_id': 'op-9'}, 'next_action': 'Inspect outcome'})
        self.assertIn('header', self.cache.ready_parts('design')['reconcile_first'])
        with self.assertRaises(ValueError):
            self.cache.part_checkpoint('design', 'header', {'status': 'complete', 'last_confirmed': 'Not reconciled'})
        with self.assertRaises(ValueError):
            self.cache.part_checkpoint('design', 'home', {'status': 'complete', 'last_confirmed': 'Children incomplete'})

    def test_reopened_part_rechecks_only_affected_parent(self):
        self.cache.plan_parts('design', self.sample_plan())
        for pid in ['header', 'products', 'cart', 'home']:
            self.cache.part_checkpoint('design', pid, {'status': 'complete', 'last_confirmed': pid + ' verified'})
        self.cache.checkpoint('design', {'status': 'complete', 'integration_check': 'Verified shared identity and assembled screens'})
        with self.assertRaises(ValueError):
            self.cache.part_checkpoint('design', 'header', {'status': 'in_progress'})
        self.cache.part_checkpoint('design', 'header', {'status': 'in_progress', 'reopen_reason': 'User requested a header edit'})
        task = self.cache.status()['state']['tasks']['design']
        self.assertEqual(task['parts']['home']['status'], 'pending')
        self.assertEqual(task['parts']['products']['status'], 'complete')
        self.assertEqual(task['parts']['cart']['status'], 'complete')
        self.assertEqual(task['status'], 'in_progress')

    def test_reopened_part_cannot_complete_using_stale_confirmation(self):
        self.cache.plan_parts('design', self.sample_plan())
        self.cache.part_checkpoint('design', 'header', {'status': 'complete', 'last_confirmed': 'Old header inspected'})
        self.cache.part_checkpoint('design', 'header', {'status': 'in_progress', 'reopen_reason': 'New user choice', 'next_action': 'Apply selected navigation'})
        with self.assertRaises(ValueError):
            self.cache.part_checkpoint('design', 'header', {'status': 'complete'})
        task = self.cache.status()['state']['tasks']['design']
        self.assertEqual(task['parts']['header']['previous_confirmation'], 'Old header inspected')
        result = self.cache.ready_parts('design')
        self.assertEqual(result['ready'][0], 'header')
        self.assertEqual(result['next_actions']['header'], 'Apply selected navigation')

    def test_readding_missing_asset_repairs_without_duplicate(self):
        entry = self.cache.add(self.asset, self.meta, shared=True)
        target = self.shared / entry['versions'][0]['asset_path']
        target.unlink()
        self.cache.add(self.asset, self.meta, shared=True)
        self.assertEqual(target.read_bytes(), self.asset.read_bytes())
        self.assertEqual(self.cache.status()['shared_references'], 1)
        target.write_text('corrupt')
        with self.assertRaises(ValueError): self.cache.add(self.asset, self.meta, shared=True)

    def test_cannot_finish_waiting_task_or_skip_integration(self):
        self.cache.checkpoint('waiting', {'status': 'waiting_for_user', 'waiting_for': 'Choose a reference'})
        with self.assertRaises(ValueError): self.cache.checkpoint('waiting', {'status': 'complete'})
        self.cache.plan_parts('design', self.sample_plan())
        for pid in ['header', 'products', 'cart', 'home']:
            self.cache.part_checkpoint('design', pid, {'status': 'complete', 'last_confirmed': pid + ' inspected'})
        with self.assertRaises(ValueError): self.cache.checkpoint('design', {'status': 'complete'})
        self.cache.checkpoint('design', {'status': 'complete', 'integration_check': 'Inspected assembled identity and composition'})

if __name__ == '__main__': unittest.main()
