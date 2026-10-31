#!/usr/bin/env python3
"""Install this Brix bundle and personal agent, preserving other configuration."""
import argparse
import json
import shutil
import tempfile
import tomllib
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def install(home):
    target = home / '.agents/skills/brix'
    agent = home / '.codex/agents/brix.toml'
    for path in (target, agent):
        if any(p.is_symlink() for p in (path, *path.parents)):
            raise SystemExit(f'Refusing symlink destination: {path}')
    bundle = target / 'references/bundle'
    wrapper = '''---
name: brix
description: Use when the user invokes brix or $brix for UI/UX research and native Figma design. One Brix agent uses shared public references and resumes each project's local progress and choices.
---

# Brix

For design work, delegate to exactly one custom agent of type `brix`, reusing it for follow-ups. If the current session has not loaded that role, use one default-role subagent named `brix` with the instructions below. If already Brix, execute directly without spawning.

Read [the canonical workflow](references/bundle/AGENTS.md). Resolve its relative skill and brief paths against `references/bundle/` beside this file. Load only relevant skills. Pass the caller's absolute project folder and requested Figma destination to Brix. The installation folder is never the design project.

Initialize/resume `.brix/` in the calling project using the bundled cache helper. Shared public-reference cache defaults to `~/.cache/brix/references`; identity, choices, fit ratings, task/part progress and Figma node IDs remain local. Reuse existing task IDs and reconcile pending writes before retrying. Do not initialize design tasks for ordinary conversation or configuration maintenance.
'''
    instructions = f'''You are Brix, the single delegated UI/UX and Figma designer. Read {bundle / 'AGENTS.md'} as your canonical workflow and resolve all its relative paths against {bundle}. Execute directly; never spawn or delegate. Use the calling project's absolute directory supplied by the parent (otherwise the working directory), never this installed bundle, for all local .brix state. Initialize or resume via {bundle / 'skills/reference-search/scripts/cache.py'}. Preserve existing project choices, identity, task IDs and per-part progress; use ~/.cache/brix/references for shared public references and quality only. Load only the routed skills needed for the task. Follow the user's selected Figma destination and report only confirmed results.'''
    agent_text = 'name = "brix"\ndescription = "Single UI/UX research and native Figma designer with shared references and per-project resume state."\ndeveloper_instructions = ' + json.dumps(instructions) + '\n'
    tomllib.loads(agent_text)
    sources = json.loads((ROOT / 'sources.json').read_text())
    with tempfile.TemporaryDirectory(prefix='brix-install-') as tmp:
        staged = Path(tmp) / 'brix'
        staged_bundle = staged / 'references/bundle'
        staged_bundle.mkdir(parents=True)
        (staged / 'SKILL.md').write_text(wrapper)
        for name in ('AGENTS.md', 'AGENT.md', 'sources.json'):
            shutil.copy2(ROOT / name, staged_bundle / name)
        for name in ('agents', 'licenses'):
            shutil.copytree(ROOT / name, staged_bundle / name)
        for entry in sources:
            name = entry['name']
            if Path(name).name != name or name in ('.', '..'):
                raise ValueError('Invalid skill name')
            source = ROOT / 'skills' / name
            if any(p.is_symlink() for p in source.rglob('*')):
                raise ValueError('Symlink in skill')
            shutil.copytree(source, staged_bundle / 'skills' / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        backup = home / '.codex/backups' / ('brix-' + stamp)
        backup.mkdir(parents=True)
        # Move only the old Brix package into a recoverable backup; no deletion.
        if target.exists():
            target.rename(backup / 'skill-brix')
        if agent.exists():
            shutil.copy2(agent, backup / 'brix.toml')
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(staged, target)
            agent.parent.mkdir(parents=True, exist_ok=True)
            agent.write_text(agent_text)
        except Exception:
            if target.exists():
                target.rename(backup / 'failed-install')
            if (backup / 'skill-brix').exists():
                (backup / 'skill-brix').rename(target)
            if (backup / 'brix.toml').exists():
                shutil.copy2(backup / 'brix.toml', agent)
            raise
        for source in staged.rglob('*'):
            if source.is_file():
                assert source.read_bytes() == (target / source.relative_to(staged)).read_bytes()
    print(json.dumps({'skill': str(target), 'agent': str(agent), 'backup': str(backup), 'skills': len(sources)}, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home(), help='User home; override for isolated installation tests')
    args = parser.parse_args()
    install(args.home.expanduser().resolve())
