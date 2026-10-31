#!/usr/bin/env python3
"""Install BRIX into one explicitly selected project; never overwrite user files."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def payloads(target):
    output = {}
    sources = json.loads((ROOT / 'sources.json').read_text())
    for entry in sources:
        name = entry['name']
        if not name or Path(name).name != name or name in ('.', '..'):
            raise ValueError(f'Invalid skill name: {name}')
        skill = ROOT / 'skills' / name
        if not (skill / 'SKILL.md').is_file():
            raise ValueError(f'Missing skill entry point: {name}')
        for source in sorted(skill.rglob('*')):
            if source.is_symlink():
                raise ValueError(f'Symlink in skill: {source}')
            if source.is_file() and '__pycache__' not in source.parts and source.suffix != '.pyc':
                output[target / '.agents/skills' / name / source.relative_to(skill)] = source.read_bytes()
        if entry.get('license_file', '').startswith('licenses/'):
            output[target / entry['license_file']] = (ROOT / entry['license_file']).read_bytes()
    instructions = (ROOT / 'AGENTS.md').read_text().replace(
        '`skills/', '`.agents/skills/')
    output[target / 'AGENTS.md'] = instructions.encode()
    output[target / 'agents/brix.md'] = (ROOT / 'agents/brix.md').read_bytes()
    for entry in sources:
        if entry.get('license_file', '').startswith('skills/'):
            entry['license_file'] = '.agents/' + entry['license_file']
    output[target / 'sources.json'] = (json.dumps(sources, indent=2) + '\n').encode()
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
