"""A public release must not carry private routes, symlinks or changed content."""
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tarfile
import unittest

spec = importlib.util.spec_from_file_location('deployment', Path(__file__).resolve().parents[1] / 'scripts/deploy_release.py')
deployment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deployment)
SOURCE = 'a' * 40


def bundle(change=None, member_type=None, audience="public"):
    files = {name: b'' for name in deployment.ASSETS}
    files['index.html'] = b'<h1>API</h1>'
    files['openapi.json'] = b'{"info":{"version":"test"},"paths":{}}'
    files['search.json'] = b'[]'
    files['build-info.json'] = json.dumps({'audience': audience, 'contract_sha256': hashlib.sha256(files['openapi.json']).hexdigest(), 'pages': 2}).encode()
    manifest = {'source_commit': SOURCE, 'files': {name: hashlib.sha256(content).hexdigest() for name, content in files.items()}}
    files['manifest.json'] = json.dumps(manifest).encode()
    if change:
        change(files)
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode='w:gz') as archive:
        for name, content in files.items():
            item = tarfile.TarInfo(name)
            item.size = len(content)
            if member_type and name == 'app.js':
                item.type, item.linkname, item.size = member_type, 'private.txt', 0
            archive.addfile(item, io.BytesIO(content))
    data = output.getvalue()
    return data, hashlib.sha256(data).hexdigest()


class PublicArchiveTests(unittest.TestCase):
    def test_valid_public_release(self):
        data, sha = bundle()
        self.assertEqual(set(deployment.verify(data, sha, SOURCE)), deployment.ASSETS)

    def test_correct_hashes_do_not_make_internal_content_public(self):
        data, sha = bundle(audience="internal")
        with self.assertRaisesRegex(ValueError, "public API audience"):
            deployment.verify(data, sha, SOURCE)

    def test_wrong_archive_hash_or_source_is_rejected(self):
        data, sha = bundle()
        for expected, source in [('0' * 64, SOURCE), (sha, 'b' * 40)]:
            with self.assertRaises(ValueError):
                deployment.verify(data, expected, source)

    def test_private_routes_and_traversal_are_rejected(self):
        for name in ['operations/diagnostics/index.html', '../private.txt', '/private.txt']:
            data, sha = bundle(lambda files: files.update({name: b'private'}))
            with self.subTest(name=name), self.assertRaises(ValueError):
                deployment.verify(data, sha, SOURCE)

    def test_symlinks_and_changed_files_are_rejected(self):
        for data, sha in [bundle(member_type=tarfile.SYMTYPE), bundle(lambda files: files.update({'app.js': b'changed'}))]:
            with self.assertRaises(ValueError):
                deployment.verify(data, sha, SOURCE)


if __name__ == '__main__':
    unittest.main()
