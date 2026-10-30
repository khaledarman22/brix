#!/usr/bin/env python3
"""Install BRIX into one explicitly selected project; never overwrite user files."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def payloads(target):
    entry_root = target / '.agents/skills/brix'
    bundle = entry_root / 'references/bundle'
    output = {}
    for folder in ['skills', 'agents']:
        for source in (ROOT / folder).rglob('*'):
            if source.is_file() and '__pycache__' not in source.parts and source.suffix != '.pyc':
                output[bundle / source.relative_to(ROOT)] = source.read_bytes()
    for name in ['AGENT.md', 'sources.json']:
        output[bundle / name] = (ROOT / name).read_bytes()
    output[entry_root / 'SKILL.md'] = (
        '---\nname: brix\ndescription: Execute UI/UX research and Figma design tasks with the Brix skill suite.\n---\n\n'
        '# Brix\n\nRead [the canonical Brix instructions](references/bundle/AGENT.md) before execution. '
        'Resolve all bundle paths from `references/bundle/` next to this skill. '
        'Load relevant designated skills from that bundle. Keep work artifacts in the calling project.\n').encode()
    entry = ('For Brix UI/UX tasks, load `.agents/skills/brix/SKILL.md` and follow its canonical bundle instructions.\n')
    output[target / 'AGENTS.md'] = entry.encode()
    output[target / 'GEMINI.md'] = entry.encode()
    output[target / '.opencode/agents/brix.md'] = (
        '---\ndescription: Brix UI/UX and Figma orchestrator\nmode: primary\n---\n\n'
        + entry).encode()
    return output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--check', action='store_true', help='Verify an existing installation without writing')
    parser.add_argument('--dry-run', action='store_true', help='Check conflicts and preview without writing')
    args = parser.parse_args()
    target = args.project.expanduser().resolve()
    files = payloads(target)
    # Check all destinations before writing anything, including symlinked ancestors.
    for path, data in files.items():
        if any(p.is_symlink() for p in [path, *path.parents] if p != target.parent):
            raise SystemExit(f'Refusing symlink destination: {path}')
        if path.exists() and (not path.is_file() or path.read_bytes() != data):
            raise SystemExit(f'Existing file differs; nothing written: {path}. Use a fresh project directory.')
    if args.check:
        missing = [str(p) for p in files if not p.is_file()]
        if missing:
            raise SystemExit('Missing files: ' + ', '.join(missing[:5]))
        print(f'Verified {len(files)} files in {target}')
        return
    if args.dry_run:
        print(f'Ready to install {len(files)} files in {target}; no changes made')
        return
    for path, data in files.items():
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(f'Installed {len(files)} files in {target}. Figma connection must be configured separately.')

if __name__ == '__main__':
    main()
