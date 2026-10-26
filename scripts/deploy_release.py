"""Verify a public release archive before writing any GitHub Pages files."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import tarfile
from urllib.request import Request, urlopen

REPOSITORY = 'GuignaLabs/fithagoras-api-docs'
LIMIT = 20 * 1024 * 1024
ASSETS = {'index.html', 'api/index.html', 'app.js', 'styles.css', 'favicon.svg',
          'openapi.json', 'search.json', 'build-info.json'}


def verify(data, expected, source):
    if len(data) > LIMIT or hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('Archive size or SHA256 mismatch')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        members = archive.getmembers()
        if len(members) > 256 or sum(item.size for item in members) > LIMIT:
            raise ValueError('Archive exceeds public output limits')
        for item in members:
            name = item.name
            allowed = name in ASSETS | {'manifest.json'} or re.fullmatch(r'(?:api/(?:[A-Za-z0-9_-]+/)+|quickstart/|guides/first-customer/)index\.html', name)
            if not item.isfile() or not allowed or name != PurePosixPath(name).as_posix() or '..' in PurePosixPath(name).parts or name in files:
                raise ValueError('Unapproved public archive member: ' + name)
            files[name] = archive.extractfile(item).read()
    manifest = json.loads(files.pop('manifest.json'))
    if manifest.get('source_commit') != source or set(manifest.get('files', {})) != set(files):
        raise ValueError('Manifest source or file inventory mismatch')
    if not ASSETS <= set(files):
        raise ValueError('Required public assets are missing')
    for name, content in files.items():
        if hashlib.sha256(content).hexdigest() != manifest['files'][name]:
            raise ValueError('Public file hash mismatch: ' + name)
    info = json.loads(files['build-info.json'])
    if info.get('audience') != 'public' or info.get('contract_sha256') != hashlib.sha256(files['openapi.json']).hexdigest():
        raise ValueError('Artifact is not the verified public API audience')
    if info.get('pages') != sum(name.endswith('.html') for name in files):
        raise ValueError('Public page count mismatch')
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'docs-[0-9a-f]{40}', args.tag):
        raise ValueError('Use an immutable docs-<source-commit> release')
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    if os.environ.get('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    with urlopen(Request(f'https://api.github.com/repos/{REPOSITORY}/releases/tags/{args.tag}', headers=headers), timeout=30) as response:
        release = json.load(response)
    checksum = re.search(r'^Artifact SHA256: ([0-9a-f]{64})$', release.get('body', ''), re.M)
    assets = [item for item in release['assets'] if item['name'] == 'public-api-docs.tar.gz']
    if not checksum or len(assets) != 1:
        raise ValueError('Release must identify exactly one reviewed archive and SHA256')
    url = assets[0]['browser_download_url']
    if not url.startswith(f'https://github.com/{REPOSITORY}/releases/download/{args.tag}/'):
        raise ValueError('Unexpected public artifact location')
    # The public download deliberately carries no API credential through redirects.
    with urlopen(url, timeout=60) as response:
        data = response.read(LIMIT + 1)
    files = verify(data, checksum[1], args.tag[5:])
    if args.output.exists() and any(args.output.iterdir()):
        raise ValueError('Refuse to overwrite an existing site directory')
    for name, content in files.items():
        target = args.output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    print(json.dumps({'result': 'PASS', 'source_commit': args.tag[5:], 'files': len(files)}))


if __name__ == '__main__':
    main()
