#!/usr/bin/env python3
"""Prepare a pinned real Git OAuth helper and local-only browser-opening shim."""
import pathlib,subprocess,shutil,urllib.request,hashlib,tarfile,io,os
p=pathlib.Path('.tools');p.mkdir(exist_ok=True)
go=shutil.which('go')
if not go:
 go=str((p/'go/bin/go').resolve())
 if not pathlib.Path(go).exists():
  b=urllib.request.urlopen('https://go.dev/dl/go1.27.2.linux-amd64.tar.gz').read()
  assert hashlib.sha256(b).hexdigest()=='ecbadb99091a3f46e31f5f934b068b1864eafa7995211b39eaddf76996045fe5'
  tarfile.open(fileobj=io.BytesIO(b),mode='r:gz').extractall(p,filter='data')
source=p/'git-credential-oauth-source';build=p/'git-credential-oauth-build';ref='031d9b7e782a4e56e71e209ea9e587f3f73adaee'
if not source.exists():subprocess.run(['git','clone','--depth','1','--no-checkout','https://github.com/hickford/git-credential-oauth.git',str(source)],check=True)
if not build.exists():
 subprocess.run(['git','-C',str(source),'fetch','--depth','1','origin',ref],check=True)
 subprocess.run(['git','-C',str(source),'worktree','add','--detach',str(build.resolve()),ref],check=True)
assert subprocess.check_output(['git','-C',str(build),'rev-parse','HEAD']).decode().strip()==ref
flags=dict(os.environ,GOMAXPROCS='2',CGO_ENABLED='0',GOPATH=str((p/'gopath').resolve()),GOCACHE=str((p/'gocache').resolve()))
subprocess.run([go,'test','-mod=readonly','./...'],cwd=build,env=flags,check=True)
subprocess.run([go,'build','-mod=readonly','-o',str((p/'git-credential-oauth').resolve()),'.'],cwd=build,env=flags,check=True)
shim=p/'shims/xdg-open';shim.parent.mkdir(exist_ok=True)
shim.write_text('#!/usr/bin/env python3'+chr(10)+'import sys,urllib.request'+chr(10)+"urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:7180/',data=sys.argv[1].encode()),timeout=10).read()"+chr(10));shim.chmod(0o700)
print('Pinned helper prepared; use only with the isolated local WordPress test server')
