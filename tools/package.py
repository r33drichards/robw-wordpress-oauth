#!/usr/bin/env python3
import pathlib,zipfile,hashlib
root=pathlib.Path('robw-oauth');out=pathlib.Path('dist/robw-oauth.zip');out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED)as z:
 for p in sorted(root.rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(root).as_posix()
  if rel.startswith('vendor/oauth2-server/')and not(rel.startswith('vendor/oauth2-server/src/')or rel=='vendor/oauth2-server/LICENSE'):continue
  info=zipfile.ZipInfo('robw-oauth/'+rel,(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,p.read_bytes())
with zipfile.ZipFile(out)as z:
 assert all('/tests/'not in n and '/mu/'not in n for n in z.namelist())
print(out,out.stat().st_size,hashlib.sha256(out.read_bytes()).hexdigest())
