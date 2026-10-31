#!/usr/bin/env python3
"""Project resume state plus a shared, content-addressed public-reference cache."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile

SCHEMA = 2

def now():
    return datetime.now(timezone.utc).isoformat()

def read(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text())

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix='.write-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)
    finally:
        Path(temp).unlink(missing_ok=True)

@contextmanager
def locked(folder):
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / '.lock').open('a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        yield
        fcntl.flock(f, fcntl.LOCK_UN)

def digest(data):
    return hashlib.sha256(data).hexdigest()

class Cache:
    def __init__(self, project, shared_root=None):
        self.project = Path(project).expanduser().resolve()
        if not self.project.is_dir():
            raise ValueError('Project directory must already exist')
        self.local = self.project / '.brix'
        config = read(self.local / 'cache.json', {})
        self.shared = Path(shared_root or config.get('shared_root') or
                           '~/.cache/brix/references').expanduser().resolve()
        if self.shared == self.local or self.local in self.shared.parents or self.shared in self.local.parents:
            raise ValueError('Shared cache must be separate from project state')

    def init(self):
        with locked(self.shared):
            path = self.shared / 'catalog.json'
            data = read(path)
            if data is None:
                write(path, {'schema_version': SCHEMA, 'references': []})
            elif data.get('schema_version') != SCHEMA:
                raise ValueError('Unsupported shared schema; preserve it and migrate explicitly')
        with locked(self.local):
            config_path = self.local / 'cache.json'
            config = read(config_path, {})
            config.update({'schema_version': SCHEMA, 'shared_root': str(self.shared)})
            write(config_path, config)
            catalog_path = self.local / 'references/catalog.json'
            catalog = read(catalog_path)
            if catalog is None:
                catalog = {'schema_version': SCHEMA, 'briefs': [], 'references': [],
                           'evaluations': [], 'boards': [], 'selections': []}
            elif catalog.get('schema_version') == 1:
                backup = catalog_path.with_name('catalog.v1.backup.json')
                if not backup.exists():
                    write(backup, catalog)
                catalog['schema_version'] = SCHEMA
            elif catalog.get('schema_version') != SCHEMA:
                raise ValueError('Unsupported project schema; no project catalog overwritten')
            write(catalog_path, catalog)
            if not (self.local / 'state.json').exists():
                write(self.local / 'state.json', {'schema_version': SCHEMA, 'tasks': {}})
        return self.status()

    def status(self):
        return {'project': str(self.project), 'shared_root': str(self.shared),
                'state': read(self.local / 'state.json'),
                'local_references': len(read(self.local / 'references/catalog.json', {}).get('references', [])),
                'shared_references': len(read(self.shared / 'catalog.json', {}).get('references', []))}

    def add(self, asset, metadata, shared=False):
        data = Path(asset).read_bytes()
        if not data:
            raise ValueError('Empty asset')
        if not metadata.get('title'):
            raise ValueError('Reference title is required')
        if shared and (metadata.get('public_source') is not True or
                       metadata.get('source_kind') not in ('live-product', 'concept', 'gallery') or
                       not str(metadata.get('source_url', '')).startswith(('https://', 'http://'))):
            raise ValueError('Shared references require an explicitly verified public source; private uploads stay local')
        allowed = {'title', 'source_url', 'canonical_url', 'gallery_url', 'source_kind',
                   'platform', 'regions', 'tags', 'viewport', 'state', 'public_source',
                   'captured_at', 'inspected_at', 'visual_notes', 'reuse_rights'}
        if shared and set(metadata) - allowed:
            raise ValueError('Shared metadata contains project-specific or unsupported fields')
        sha = digest(data)
        identity = json.dumps([metadata.get('canonical_url') or metadata.get('source_url'),
                               metadata.get('viewport'), metadata.get('state'), sha], sort_keys=True)
        rid = 'ref-' + digest(identity.encode())[:24]
        suffix = Path(asset).suffix.lower()
        if suffix not in ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif'):
            raise ValueError('Use an image asset with a recognized extension')
        folder = self.shared if shared else self.local / 'references'
        lock_root = self.shared if shared else self.local
        with locked(lock_root):
            path = folder / 'catalog.json'
            catalog = read(path)
            if catalog is None:
                raise ValueError('Run init first')
            existing = next((r for r in catalog['references'] if r['id'] == rid), None)
            if existing:
                version = existing['versions'][0]
                cached = ((self.shared if shared else self.project) / version['asset_path']).resolve()
                base = self.shared if shared else self.project
                if base not in cached.parents:
                    raise ValueError('Cached asset path escapes its cache/project')
                if cached.exists() and digest(cached.read_bytes()) != version['sha256']:
                    raise ValueError('Existing cached asset is corrupt')
                if not cached.exists():
                    cached.parent.mkdir(parents=True, exist_ok=True)
                    fd, tmp = tempfile.mkstemp(prefix='.repair-', dir=cached.parent)
                    try:
                        with os.fdopen(fd, 'wb') as f:
                            f.write(data)
                        os.replace(tmp, cached)
                    finally:
                        Path(tmp).unlink(missing_ok=True)
                return existing
            asset_path = Path('assets') / sha / ('capture' + suffix)
            destination = folder / asset_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() and digest(destination.read_bytes()) != sha:
                raise ValueError('Existing cached asset is corrupt; do not overwrite silently')
            if not destination.exists():
                fd, tmp = tempfile.mkstemp(prefix='.asset-', dir=destination.parent)
                try:
                    with os.fdopen(fd, 'wb') as f:
                        f.write(data)
                        f.flush()
                        os.fsync(f.fileno())
                    os.replace(tmp, destination)
                finally:
                    Path(tmp).unlink(missing_ok=True)
            entry = dict(metadata)
            entry.update({'id': rid, 'versions': [{'id': sha, 'sha256': sha,
                'asset_path': str(asset_path) if shared else str(destination.relative_to(self.project)),
                'captured_at': metadata.get('captured_at', now()),
                'inspected_at': metadata.get('inspected_at'), 'viewport': metadata.get('viewport'),
                'state': metadata.get('state')} ]})
            catalog['references'].append(entry)
            write(path, catalog)
            return entry

    def find(self, query):
        words = query.casefold().split()
        found, seen = [], set()
        for scope, path in [('local', self.local / 'references/catalog.json'),
                            ('shared', self.shared / 'catalog.json')]:
            for entry in read(path, {}).get('references', []):
                searchable = json.dumps({k: entry.get(k) for k in
                    ('title', 'platform', 'regions', 'tags', 'visual_notes')}, ensure_ascii=False).casefold()
                if all(word in searchable for word in words) and entry['id'] not in seen:
                    found.append({'scope': scope, 'reference': entry})
                    seen.add(entry['id'])
        return found

    def reuse(self, reference_id):
        shared = read(self.shared / 'catalog.json', {'references': []})
        entry = next((r for r in shared['references'] if r['id'] == reference_id), None)
        if entry is None:
            raise ValueError('Shared reference not found')
        copied = json.loads(json.dumps(entry))
        # Read and verify all assets before touching the project catalog.
        assets = []
        for version in copied['versions']:
            src = (self.shared / version['asset_path']).resolve()
            if self.shared not in src.parents:
                raise ValueError('Asset path escapes shared cache')
            data = src.read_bytes()
            if digest(data) != version['sha256']:
                raise ValueError('Shared asset hash mismatch')
            dest = self.local / 'references/assets' / version['sha256'] / src.name
            assets.append((dest, data))
            version['asset_path'] = str(dest.relative_to(self.project))
        copied['shared_origin'] = {'reference_id': reference_id}
        with locked(self.local):
            path = self.local / 'references/catalog.json'
            catalog = read(path)
            if catalog is None:
                raise ValueError('Run init first')
            for dest, data in assets:
                dest.parent.mkdir(parents=True, exist_ok=True)
                if dest.exists() and digest(dest.read_bytes()) != digest(data):
                    raise ValueError('Local asset hash mismatch')
                if not dest.exists():
                    fd, tmp = tempfile.mkstemp(prefix='.asset-', dir=dest.parent)
                    try:
                        with os.fdopen(fd, 'wb') as f:
                            f.write(data)
                        os.replace(tmp, dest)
                    finally:
                        Path(tmp).unlink(missing_ok=True)
            existing = next((r for r in catalog['references'] if r['id'] == reference_id), None)
            if existing:
                reviews = existing.setdefault('quality_reviews', [])
                for review in copied.get('quality_reviews', []):
                    if review not in reviews:
                        reviews.append(review)
                write(path, catalog)
                return existing
            catalog['references'].append(copied)
            write(path, catalog)
        return copied

    def review(self, reference_id, review, shared=False):
        """Store intrinsic visual quality separately from project fit and user choices."""
        allowed = {'version_id', 'verdict', 'scores', 'strengths', 'weaknesses',
                   'useful_regions', 'avoid_regions', 'evidence', 'inspected_at'}
        if set(review) - allowed:
            raise ValueError('Quality review contains unsupported/project-specific fields')
        if review.get('verdict') not in {'strong', 'mixed', 'weak', 'unreviewed'}:
            raise ValueError('Invalid quality verdict')
        scores = review.get('scores', {})
        if not isinstance(scores, dict) or set(scores) - {'layout', 'typography', 'spacing', 'visual_clarity'}:
            raise ValueError('Use intrinsic visual-quality criteria only')
        if any(v is not None and (type(v) is not int or not 1 <= v <= 5) for v in scores.values()):
            raise ValueError('Scores must be integers 1..5 or null')
        if review['verdict'] != 'unreviewed' and (not review.get('evidence') or not review.get('inspected_at')):
            raise ValueError('A rated reference needs observed evidence and inspection time')
        folder = self.shared if shared else self.local / 'references'
        with locked(self.shared if shared else self.local):
            path = folder / 'catalog.json'
            catalog = read(path)
            if catalog is None:
                raise ValueError('Run init first')
            entry = next((r for r in catalog['references'] if r['id'] == reference_id), None)
            if entry is None or not any(v['id'] == review.get('version_id') for v in entry['versions']):
                raise ValueError('Reference/version not found in selected cache')
            reviews = entry.setdefault('quality_reviews', [])
            if review not in reviews:
                reviews.append(review)
                write(path, catalog)
            return entry

    @staticmethod
    def search_key(request):
        allowed = {'source', 'query', 'filters', 'public_source'}
        if set(request) - allowed or not request.get('source') or not isinstance(request.get('query'), str):
            raise ValueError('Search request needs source/query and optional filters/public_source')
        canonical = {'source': request['source'],
                     'query': ' '.join(request['query'].casefold().split()),
                     'filters': request.get('filters', {})}
        return 'search-' + digest(json.dumps(canonical, sort_keys=True).encode())[:24]

    def search_log(self, request, page=None, shared=False):
        """Lookup or record observed pagination; never performs network requests."""
        key = self.search_key(request)
        if shared and request.get('public_source') is not True:
            raise ValueError('Shared search history requires a public, non-project-specific query')
        folder = self.shared if shared else self.local / 'references'
        lock_root = self.shared if shared else self.local
        path = folder / 'searches.json'
        if page is None:
            return read(path, {'searches': {}})['searches'].get(key)
        allowed = {'request_token', 'url', 'pagination_mode', 'result_ids', 'next_token',
                   'outcome', 'end_confirmed', 'coverage_satisfied', 'reason', 'retry_after', 'observed_at'}
        if set(page) - allowed or not isinstance(page.get('request_token'), str):
            raise ValueError('Page requires a stable observed request_token; unsupported fields rejected')
        if page.get('outcome') not in {'visited', 'blocked', 'failed'}:
            raise ValueError('Page outcome must be visited/blocked/failed')
        if page.get('pagination_mode') not in {'numbered', 'next-link', 'cursor', 'load-more', 'infinite-scroll', 'none'}:
            raise ValueError('Unknown pagination mode')
        if not isinstance(page.get('result_ids', []), list) or not page.get('observed_at'):
            raise ValueError('Record result_ids and actual observation time')
        if page.get('end_confirmed') and page.get('next_token') is not None:
            raise ValueError('Cannot claim end while another page is known')
        with locked(lock_root):
            if not (folder / 'catalog.json').exists():
                raise ValueError('Run init first')
            log = read(path, {'schema_version': SCHEMA, 'searches': {}})
            item = log['searches'].setdefault(key, {'id': key, 'request': request, 'pages': [],
                                                   'status': 'active', 'next_token': None})
            # An already-recorded identical observation is idempotent. Differing new
            # observations are retained so a failed attempt never erases visited evidence.
            if page in item['pages']:
                return item
            item['pages'].append(page)
            visited = {p['request_token'] for p in item['pages'] if p['outcome'] == 'visited'}
            item['result_ids'] = list(dict.fromkeys(rid for p in item['pages'] for rid in p.get('result_ids', [])))
            item['visited_tokens'] = sorted(visited)
            item['next_token'] = page.get('next_token')
            item['updated_at'] = now()
            item['retry_after'] = page.get('retry_after')
            item['reason'] = page.get('reason')
            if page['outcome'] != 'visited':
                item['status'] = page['outcome']
                item['next_token'] = page['request_token']
            elif page.get('end_confirmed'):
                item['status'] = 'exhausted'
            elif page.get('coverage_satisfied'):
                item['status'] = 'covered'
            elif page.get('next_token') in visited:
                item['status'] = 'paused'
                item['reason'] = 'Pagination loop detected; inspect navigation before continuing'
            elif page.get('next_token') is None:
                item['status'] = 'paused'
                item['reason'] = 'Next page unknown; do not assume exhaustion'
            else:
                item['status'] = 'active'
            write(path, log)
            return item

    @staticmethod
    def validate_parts(parts):
        edges = {}
        for pid, part in parts.items():
            parent = part.get('parent_id')
            deps = part.get('depends_on', [])
            if not isinstance(deps, list) or any(d not in parts or d == pid for d in deps):
                raise ValueError('Part dependency is missing or self-referential')
            if parent is not None and (parent not in parts or parent == pid):
                raise ValueError('Part parent is missing or self-referential')
            # A parent is complete only after its children; include that edge.
            edges[pid] = set(deps) | {k for k, v in parts.items() if v.get('parent_id') == pid}
        done, active = set(), set()
        def visit(pid):
            if pid in active:
                raise ValueError('Cyclic part hierarchy/dependencies')
            if pid in done:
                return
            active.add(pid)
            for dep in edges[pid]: visit(dep)
            active.remove(pid); done.add(pid)
        for pid in parts: visit(pid)

    @staticmethod
    def invalidate_dependents(parts):
        changed = True
        while changed:
            changed = False
            for pid, part in parts.items():
                required = part.get('depends_on', []) + [k for k, p in parts.items() if p.get('parent_id') == pid]
                if part['status'] == 'complete' and any(parts[d]['status'] != 'complete' for d in required):
                    part['previous_confirmation'] = part.get('last_confirmed')
                    part['last_confirmed'] = None
                    part.update(status='pending', next_action='Recheck affected dependency changes; preserve verified work',
                                reopen_reason='A child or required dependency changed', updated_at=now(),
                                revision=part.get('revision', 0) + 1)
                    changed = True

    def plan_parts(self, task_id, plan):
        """Upsert a scoped plan without resetting existing part progress."""
        specs = plan.get('parts')
        if not isinstance(specs, list) or not specs:
            raise ValueError('Plan requires a nonempty parts list')
        ids = [p.get('id') for p in specs]
        if any(not isinstance(pid, str) or not pid for pid in ids) or len(ids) != len(set(ids)):
            raise ValueError('Part IDs must be unique nonempty strings')
        with locked(self.local):
            path = self.local / 'state.json'
            state = read(path)
            if state is None: raise ValueError('Run init first')
            identity = state.get('identity') or plan.get('identity')
            if not isinstance(identity, dict) or not identity.get('id'):
                raise ValueError('Plan needs one project identity record; unknown bindings may remain unresolved')
            if plan.get('identity') and state.get('identity') and plan['identity'] != state['identity']:
                raise ValueError('Reuse the saved project identity; do not silently replace it in a part plan')
            task = state['tasks'].setdefault(task_id, {'status': 'in_progress'})
            parts = task.setdefault('parts', {})
            changed = False
            for spec in specs:
                if set(spec) - {'id', 'title', 'scope', 'parent_id', 'depends_on'}:
                    raise ValueError('Part plan contains unsupported fields; progress belongs in part-checkpoint')
                pid = spec['id']
                if not spec.get('title') or not spec.get('scope'):
                    raise ValueError('Every part needs title and concrete scope')
                previous = parts.get(pid)
                normalized = dict(spec, parent_id=spec.get('parent_id'), depends_on=spec.get('depends_on', []))
                if previous:
                    different = any(previous.get(k) != v for k, v in normalized.items())
                    if different and previous['status'] == 'complete':
                        raise ValueError('Reopen the completed part with a reason before changing its scope')
                    if different:
                        previous['previous_confirmation'] = previous.get('last_confirmed')
                        previous['last_confirmed'] = None
                    previous.update(normalized)
                    changed |= different
                else:
                    parts[pid] = dict(normalized, status='pending', revision=0, next_action='Start this part', pending_action=None)
                    changed = True
            self.validate_parts(parts)
            self.invalidate_dependents(parts)
            state['identity'] = identity
            task['identity_id'] = identity['id']
            if changed and task['status'] == 'complete': task['status'] = 'in_progress'
            if 'request' in plan: task['request'] = plan['request']
            task['updated_at'] = now()
            write(path, state)
            return task

    def part_checkpoint(self, task_id, part_id, update):
        statuses = {'pending', 'in_progress', 'waiting_for_user', 'blocked', 'complete'}
        if update.get('status') not in statuses:
            raise ValueError('Invalid part status')
        if set(update) & {'id', 'title', 'scope', 'parent_id', 'depends_on', 'identity', 'identity_id'}:
            raise ValueError('Use plan-parts for structure; parts inherit the project identity')
        with locked(self.local):
            path = self.local / 'state.json'
            state = read(path)
            if state is None: raise ValueError('Run init first')
            task = state['tasks'].get(task_id, {})
            parts = task.get('parts', {})
            if part_id not in parts: raise ValueError('Part not found')
            previous = parts[part_id]
            if previous['status'] == 'complete' and update['status'] != 'complete' and not update.get('reopen_reason'):
                raise ValueError('Reopening a completed part requires a reason')
            item = dict(previous); item.update(update)
            if previous['status'] == 'complete' and update['status'] != 'complete':
                item['previous_confirmation'] = previous.get('last_confirmed')
                item['last_confirmed'] = update.get('last_confirmed')
            if item['status'] in {'in_progress', 'complete'}:
                if any(parts[d]['status'] != 'complete' for d in item.get('depends_on', [])):
                    raise ValueError('Required dependencies are unfinished')
            if item['status'] == 'complete':
                if item.get('pending_action') or item.get('waiting_for') or not item.get('last_confirmed'):
                    raise ValueError('Completion requires confirmed evidence and no pending action/user choice')
                if any(p['status'] != 'complete' for p in parts.values() if p.get('parent_id') == part_id):
                    raise ValueError('Child parts are unfinished')
            item['revision'] = previous.get('revision', 0) + 1
            item['updated_at'] = now()
            parts[part_id] = item
            self.invalidate_dependents(parts)
            if item['status'] != 'complete' and task.get('status') == 'complete': task['status'] = 'in_progress'
            write(path, state)
            return item

    def ready_parts(self, task_id):
        task = read(self.local / 'state.json', {'tasks': {}})['tasks'].get(task_id, {})
        parts = task.get('parts', {})
        ready, reconcile, waiting = [], [], []
        for pid, part in parts.items():
            if part.get('pending_action'): reconcile.append(pid); continue
            if part['status'] in {'blocked', 'waiting_for_user'}: waiting.append(pid); continue
            if part['status'] == 'complete': continue
            required = part.get('depends_on', []) + [k for k, p in parts.items() if p.get('parent_id') == pid]
            if all(parts[d]['status'] == 'complete' for d in required): ready.append(pid)
        ready.sort(key=lambda pid: parts[pid]['status'] != 'in_progress')
        return {'identity_id': task.get('identity_id'), 'ready': ready, 'reconcile_first': reconcile, 'waiting': waiting,
                'next_actions': {pid: parts[pid].get('next_action') for pid in ready + reconcile + waiting}}

    def checkpoint(self, task_id, update):
        statuses = {'in_progress', 'waiting_for_user', 'blocked', 'complete'}
        if update.get('status') not in statuses:
            raise ValueError('Checkpoint needs a valid status')
        if update['status'] == 'complete' and update.get('pending_action'):
            raise ValueError('Cannot complete with an unresolved pending action')
        with locked(self.local):
            path = self.local / 'state.json'
            state = read(path)
            if state is None:
                raise ValueError('Run init first')
            previous = state['tasks'].get(task_id, {})
            item = dict(previous)
            item.update(update)
            if item['status'] == 'complete' and (item.get('pending_action') or item.get('waiting_for')):
                raise ValueError('Clear pending actions and user choices explicitly before completion')
            if item['status'] == 'complete' and any(p['status'] != 'complete' for p in item.get('parts', {}).values()):
                raise ValueError('Cannot complete a task with unfinished parts')
            if item['status'] == 'complete' and item.get('parts') and not update.get('integration_check'):
                raise ValueError('Part-based task completion requires a fresh integration_check')
            if 'parts' in update or 'identity_id' in update:
                raise ValueError('Use plan-parts/part-checkpoint to preserve part invariants')
            item['updated_at'] = now()
            item['revision'] = previous.get('revision', 0) + 1
            state['tasks'][task_id] = item
            write(path, state)
        return item

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True)
    parser.add_argument('--shared-root')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('init')
    sub.add_parser('status')
    p = sub.add_parser('find'); p.add_argument('query')
    p = sub.add_parser('add'); p.add_argument('--asset', required=True); p.add_argument('--metadata', required=True); p.add_argument('--shared', action='store_true')
    p = sub.add_parser('reuse'); p.add_argument('reference_id')
    p = sub.add_parser('checkpoint'); p.add_argument('task_id'); p.add_argument('--data', required=True)
    p = sub.add_parser('review'); p.add_argument('reference_id'); p.add_argument('--data', required=True); p.add_argument('--shared', action='store_true')
    p = sub.add_parser('search-log'); p.add_argument('--request', required=True); p.add_argument('--page'); p.add_argument('--shared', action='store_true')
    p = sub.add_parser('plan-parts'); p.add_argument('task_id'); p.add_argument('--data', required=True)
    p = sub.add_parser('part-checkpoint'); p.add_argument('task_id'); p.add_argument('part_id'); p.add_argument('--data', required=True)
    p = sub.add_parser('ready-parts'); p.add_argument('task_id')
    args = parser.parse_args()
    try:
        cache = Cache(args.project, args.shared_root)
        if args.command == 'init': result = cache.init()
        elif args.command == 'status': result = cache.status()
        elif args.command == 'find': result = cache.find(args.query)
        elif args.command == 'add': result = cache.add(args.asset, read(Path(args.metadata)), args.shared)
        elif args.command == 'reuse': result = cache.reuse(args.reference_id)
        elif args.command == 'review': result = cache.review(args.reference_id, read(Path(args.data)), args.shared)
        elif args.command == 'search-log': result = cache.search_log(read(Path(args.request)), read(Path(args.page)) if args.page else None, args.shared)
        elif args.command == 'plan-parts': result = cache.plan_parts(args.task_id, read(Path(args.data)))
        elif args.command == 'part-checkpoint': result = cache.part_checkpoint(args.task_id, args.part_id, read(Path(args.data)))
        elif args.command == 'ready-parts': result = cache.ready_parts(args.task_id)
        else: result = cache.checkpoint(args.task_id, read(Path(args.data)))
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError) as e:
        parser.exit(1, f'Cache error: {e}\n')

if __name__ == '__main__':
    main()
