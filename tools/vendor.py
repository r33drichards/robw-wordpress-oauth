#!/usr/bin/env python3
"""Rebuild only vendored library sources from pinned upstream archive; no deployment."""
import pathlib,urllib.request,hashlib,zipfile,io,shutil,json
ref='1c715c2d2f71254d1c683b8c89a0f16b61ccd0d6'
expected='1a58d3081899be3b4f95cce848916b0eb809fe67afe2c9e9cffbeeb139bbdeb3'
b=urllib.request.urlopen('https://codeload.github.com/bshaffer/oauth2-server-php/zip/'+ref).read()
assert hashlib.sha256(b).hexdigest()==expected,'Upstream archive drift'
z=zipfile.ZipFile(io.BytesIO(b));prefix=z.namelist()[0]
out=pathlib.Path('robw-oauth/vendor/oauth2-server')
if out.exists():shutil.rmtree(out)
for name in z.namelist():
 if name.endswith('/'):continue
 rel=name[len(prefix):];
 if not(rel.startswith('src/')or rel=='LICENSE'):continue
 p=out/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(name))
bs=chr(92)
for p in (out/'src').rglob('*.php'):
 s=p.read_text().replace('OAuth2'+bs,'RobwOAuthVendor'+bs+'OAuth2'+bs).replace('namespace OAuth2;','namespace RobwOAuthVendor'+bs+'OAuth2;');p.write_text(s)
print('Pinned MIT library rebuilt with isolated namespace; rerun all tests')
