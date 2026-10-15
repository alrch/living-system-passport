#!/usr/bin/env python3
"""Snapshot exact reviewed files and optional Git revisions; never accept a review."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone


def contained(root, value):
    path = Path(value)
    path = (root / path).resolve() if not path.is_absolute() else path.resolve()
    if not path.is_relative_to(root):
        raise ValueError(f'path is outside root: {value}')
    return path


def digest(path):
    if not path.is_file():
        raise ValueError(f'not a readable file: {path}')
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def revision(path):
    # Exact roots prevent accidentally attributing a directory to its parent repo.
    def git(*args):
        return subprocess.run(['git', '-C', str(path), *args], check=True,
                              capture_output=True, text=True, timeout=10).stdout.strip()
    if Path(git('rev-parse', '--show-toplevel')).resolve() != path:
        raise ValueError(f'not an exact repository root: {path}')
    return git('rev-parse', 'HEAD')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['capture', 'check'])
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--file', action='append', default=[],
                        help='Exact input, relative to root; repeat for passport and sources')
    parser.add_argument('--repository', action='append', default=[],
                        help='Exact Git root, relative to root; optional and repeatable')
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error('root must be an existing directory')
    snapshot = contained(root, args.snapshot)
    if args.action == 'capture':
        if not args.file:
            parser.error('capture requires at least one --file')
        if snapshot.exists():
            parser.error('snapshot already exists; use a new evidence path')
        paths = {contained(root, item) for item in args.file}
        if snapshot in paths:
            parser.error('snapshot cannot be one of its own inputs')
        files = {str(path.relative_to(root)): digest(path) for path in sorted(paths)}
        repos = {str(path.relative_to(root)): revision(path)
                 for path in sorted({contained(root, item) for item in args.repository})}
        data = dict(schema_version=1, captured_at=datetime.now(timezone.utc).isoformat(),
                    scope='exact file hashes and optional Git HEADs; no new-file discovery or semantic approval',
                    files=files, repositories=repos)
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation keeps old evidence immutable even across concurrent captures.
        with snapshot.open('x') as stream:
            json.dump(data, stream, indent=2, ensure_ascii=False)
            stream.write('\n')
        print(json.dumps(dict(captured_files=len(files), repositories=len(repos))))
        return 0

    if args.file or args.repository:
        parser.error('check uses the recorded input scope; no --file/--repository')
    data = json.loads(snapshot.read_text())
    if not isinstance(data, dict) or data.get('schema_version') != 1 or not isinstance(data.get('files'), dict) or not data['files']:
        raise ValueError('unsupported or empty snapshot')
    if not isinstance(data.get('repositories'), dict):
        raise ValueError('invalid repository snapshot')
    changes = []
    for name, expected in data['files'].items():
        path = contained(root, name)
        if not isinstance(expected, str) or len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
            raise ValueError(f'invalid SHA256 for {name}')
        if not path.is_file():
            changes.append(dict(kind='missing_file', path=name))
        elif digest(path) != expected:
            changes.append(dict(kind='changed_file', path=name))
    for name, expected in data['repositories'].items():
        path = contained(root, name)
        try:
            current = revision(path)
        except (ValueError, subprocess.SubprocessError, OSError):
            changes.append(dict(kind='unavailable_repository', path=name))
            continue
        if current != expected:
            changes.append(dict(kind='changed_revision', path=name,
                                expected=expected, actual=current))
    print(json.dumps(dict(unchanged=not changes, changes=changes,
                          scope=data.get('scope')), ensure_ascii=False))
    return 1 if changes else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(f'evidence snapshot: {exc}', file=sys.stderr)
        sys.exit(2)
