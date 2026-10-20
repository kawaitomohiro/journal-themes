#!/usr/bin/env python3
"""index.html を作る。
  高学年200: data_src/original.html の BUILTIN から取り出す（段階は目安をタグから付ける）
  低学年100・中学年100: data_src/themes_low_mid.py
使い方: python3 build.py
"""
import re, sys, json, pathlib
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here / 'data_src'))
from themes_low_mid import LOW_THEMES, MID_THEMES  # noqa

html = (here / 'data_src' / 'original.html').read_text(encoding='utf-8')
m = re.search(r'const BUILTIN = (\[.*?\]);', html, re.S)
if not m:
    sys.exit('BUILTIN が見つかりません')
high = json.loads(m.group(1))

def stage_of_high(x):
    """高学年200本の段階（目安）: 発展期 > 展開期 > 導入期 の順に判定"""
    tags, per = set(x['tags']), set(x['per'])
    if per & {'学期おわり', '卒業・進級'} or tags & {'将来・仕事', '社会・世の中', '探究・問い'}:
        return '発展'
    if tags & {'他者から学ぶ', '失敗・つまずき', '目標・自己調整', 'リーダー・役割', '学級づくり'}:
        return '展開'
    return '導入'

for x in high:
    x['key'] = 'B' + str(x['n'])
    x['grade'] = '高'
    x['stage'] = stage_of_high(x)
for x in LOW_THEMES: x['grade'] = '低'
for x in MID_THEMES: x['grade'] = '中'

allthemes = LOW_THEMES + MID_THEMES + high
keys = [x['key'] for x in allthemes]
assert len(keys) == len(set(keys)), '重複キー'
builtin = json.dumps(allthemes, ensure_ascii=False, separators=(',', ':'))

tpl = (here / 'src' / 'app.html').read_text(encoding='utf-8')
assert '/*__BUILTIN__*/' in tpl
out = tpl.replace('/*__BUILTIN__*/', 'const BUILTIN = ' + builtin + ';')
(here / 'index.html').write_text(out, encoding='utf-8')
from collections import Counter
print(f'index.html を作りました（テーマ {len(allthemes)} 件・{len(out):,} 文字）')
print(' 学年:', dict(Counter(x["grade"] for x in allthemes)))
print(' 段階:', {g: dict(Counter(x["stage"] for x in allthemes if x["grade"] == g)) for g in "低中高"})
