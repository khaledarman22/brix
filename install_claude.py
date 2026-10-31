#!/usr/bin/env python3
"""Install the current Brix suite for Claude Code with recoverable backups."""
import argparse
import json
import shutil
import tempfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def install(home):
    base = home / '.claude'
    bundle = base / 'skill-bundles/brix'
    agent = base / 'agents/brix.md'
    skill = base / 'skills/brix'
    for dest in (bundle, agent, skill):
        if any(p.is_symlink() for p in (dest, *dest.parents)):
            raise ValueError(f'Refusing symlink destination: {dest}')
    brief = f'''# Brix

You are the single Brix designer. Execute directly without spawning more agents. Before work, read `{bundle}/AGENTS.md`; resolve its relative paths against `{bundle}`, not the calling project. Load only the routed skills needed. Do not substitute legacy Brix or ui-ux-magec workflows.

Use the calling project's absolute directory for `.brix/` state and deliverables. Run `python3 -B {bundle}/skills/reference-search/scripts/cache.py --project /absolute/calling-project init` only when needed, then resume existing task/part IDs and choices. Shared public references and quality use `~/.cache/brix/references`; choices, identity and progress stay local. Reconcile pending Figma writes before replay.

Before new or materially redesigned product screens, show real references and ratings on the Figma References page and return its link. Save waiting_for_user and wait for explicit user choice before applying that scope. A section outline or palette does not bypass this gate. Preserve already explicit selections and scoped user exceptions. If reference presentation is blocked, report it; do not silently design instead.

When images are needed, read `{bundle}/skills/image-prompts/SKILL.md`, write complete prompts in the calling project's `deliverables/image-prompts/<task-id>.md`, and return a clickable absolute file link. Prompt completion is distinct from generating or applying images. Follow the canonical cache protocol for progress. Return the board/prompt/output links and confirmed progress to the parent, including outstanding user choices.
'''
    wrapper = f'''---
name: brix
description: Use Brix for UI/UX research and native Figma design with user-selected references, shared cache, per-project resume and complete image prompt files.
---
# Invoke Brix

For design work, delegate to the single `brix` subagent and reuse it for follow-ups. Pass the calling project's absolute folder, user brief, attachments, Figma destination, existing choices and exact user feedback. Require it to read `{bundle}/AGENTS.md` before work. If already acting as Brix, execute directly without redelegation.

Relay Brix's References page and ask for the user's choice before product design; never choose on their behalf or treat your section outline as their approval. Preserve scoped existing explicit choices. Relay the image-prompts file link when delivered. On resume, restore the project's `.brix/` state, not remembered instructions from an old bundle. Skill/configuration maintenance may be handled directly.
'''
    entries = json.loads((ROOT/'sources.json').read_text())
    with tempfile.TemporaryDirectory(prefix='brix-claude-') as tmp:
        stage = Path(tmp)
        staged = stage/'bundle'; staged.mkdir()
        for name in ('AGENTS.md','AGENT.md','sources.json'):
            shutil.copy2(ROOT/name, staged/name)
        for name in ('agents','licenses'):
            shutil.copytree(ROOT/name, staged/name)
        for entry in entries:
            name = entry['name']
            if Path(name).name != name or name in ('.','..'):
                raise ValueError('Invalid skill name')
            source = ROOT/'skills'/name
            if any(p.is_symlink() for p in source.rglob('*')):
                raise ValueError('Symlink in source')
            shutil.copytree(source, staged/'skills'/name, ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        (stage/'agent.md').write_text('---\nname: brix\ndescription: Single Brix designer; present references and wait for user selection, resume cached project progress, and deliver complete image prompts.\n---\n\n'+brief)
        (stage/'skill').mkdir(); (stage/'skill/SKILL.md').write_text(wrapper)
        backup = base/'backups'/('brix-'+datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
        backup.mkdir(parents=True)
        pairs = [(staged,bundle,'bundle'),(stage/'agent.md',agent,'agent.md'),(stage/'skill',skill,'skill')]
        changed = []
        try:
            for src,dest,label in pairs:
                dest.parent.mkdir(parents=True,exist_ok=True)
                had_old = dest.exists()
                if had_old: dest.rename(backup/label)
                changed.append((dest,label,had_old))
                if src.is_dir(): shutil.copytree(src,dest)
                else: shutil.copy2(src,dest)
            for src,dest,_ in pairs:
                files = src.rglob('*') if src.is_dir() else [src]
                for file in files:
                    if file.is_file():
                        installed = dest/file.relative_to(src) if src.is_dir() else dest
                        assert file.read_bytes()==installed.read_bytes()
        except Exception:
            for dest,label,had_old in reversed(changed):
                if dest.exists(): dest.rename(backup/('failed-'+label))
                if had_old: (backup/label).rename(dest)
            raise
    print(json.dumps({'bundle':str(bundle),'agent':str(agent),'skill':str(skill),'backup':str(backup),'skill_count':len(entries)},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home',type=Path,default=Path.home())
    args=parser.parse_args()
    install(args.home.expanduser().resolve())
