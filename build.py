#!/usr/bin/env python3
"""src/app.html のひな形に、元HTML（振り返りジャーナルテーマ.html）の BUILTIN（200テーマ）を差しこんで index.html を作る。
使い方: python3 build.py [元HTMLのパス]
"""
import re, sys, pathlib
here = pathlib.Path(__file__).parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else here / 'data_src' / 'original.html'
html = src.read_text(encoding='utf-8')
m = re.search(r'const BUILTIN = (\[.*?\]);', html, re.S)
if not m:
    sys.exit('BUILTIN が見つかりません: ' + str(src))
builtin = m.group(1)
tpl = (here / 'src' / 'app.html').read_text(encoding='utf-8')
assert '/*__BUILTIN__*/' in tpl
out = tpl.replace('/*__BUILTIN__*/', 'const BUILTIN = ' + builtin + ';')
(here / 'index.html').write_text(out, encoding='utf-8')
n = builtin.count('"n":')
print(f'index.html を作りました（テーマ {n} 件・{len(out):,} 文字）')
