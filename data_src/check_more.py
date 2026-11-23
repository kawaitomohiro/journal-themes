"""追加テーマの検査: 本数・分類・低学年は漢字なし・中学年は3年までの漢字・既存との似すぎ"""
import sys, re, json, pathlib, difflib
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from themes_low_mid import LOW_THEMES, MID_THEMES
from themes_more import LOW_MORE_THEMES, MID_MORE_THEMES, HIGH_MORE_THEMES
G1="一右雨円王音下火花貝学気九休玉金空月犬見五口校左三山子四糸字耳七車手十出女小上森人水正生青夕石赤千川先早草足村大男竹中虫町天田土二日入年白八百文木本名目立力林六"
G2="引羽雲園遠何科夏家歌画回会海絵外角楽活間丸岩顔汽記帰弓牛魚京強教近兄形計元言原戸古午後語工公広交光考行高黄合谷国黒今才細作算止市矢姉思紙寺自時室社弱首秋週春書少場色食心新親図数西声星晴切雪船線前組走多太体台地池知茶昼長鳥朝直通弟店点電刀冬当東答頭同道読内南肉馬売買麦半番父風分聞米歩母方北毎妹万明鳴毛門夜野友用曜来里理話"
G3="悪安暗医委意育員院飲運泳駅央横屋温化荷界開階寒感漢館岸起期客究急級宮球去橋業曲局銀区苦具君係軽血決研県庫湖向幸港号根祭皿仕死使始指歯詩次事持式実写者主守取酒受州拾終習集住重宿所暑助昭消商章勝乗植申身神真深進世整昔全相送想息速族他打対待代第題炭短談着注柱丁帳調追定庭笛鉄転都度投豆島湯登等動童農波配倍箱畑発反坂板皮悲美鼻筆氷表秒病品負部服福物平返勉放味命面問役薬由油有遊予羊洋葉陽様落流旅両緑礼列練路和"
OK3=set(G1+G2+G3)
kan=re.compile(r'[一-鿿]')
CATS={"学びと思考","学級・クラス","生活・教科・友達","自分・将来・社会"}
err=0
for name,L,n in [('低',LOW_MORE_THEMES,100),('中',MID_MORE_THEMES,100),('高',HIGH_MORE_THEMES,100)]:
    if len(L)!=n: print(name,'本数',len(L)); err+=1
    for x in L:
        assert x['cat'] in CATS, x
        assert x['stage'] in ('導入','展開','発展'), x
        if name=='低':
            k=kan.findall(x['t'])
            if k: print('低 漢字',x['key'],k,x['t']); err+=1
        if name=='中':
            k=[c for c in kan.findall(x['t']) if c not in OK3]
            if k: print('中 4年以上の漢字',x['key'],k,x['t']); err+=1
s=open(here/'original.html',encoding='utf-8').read()
high=json.loads(re.search(r'const BUILTIN = (\[.*?\]);',s,re.S).group(1))
groups={'低':LOW_THEMES+LOW_MORE_THEMES,'中':MID_THEMES+MID_THEMES[:0]+MID_MORE_THEMES,'高':high+HIGH_MORE_THEMES}
norm=lambda t:re.sub(r'[\s、。？！「」（）・…]','',t)
for g,L in groups.items():
    new=[x for x in L if x['n']>(200 if g=='高' else 100)]
    for x in new:
        for y in L:
            if y is x or (y['n']>x['n'] and y in new): continue
            r=difflib.SequenceMatcher(None,norm(x['t']),norm(y['t'])).ratio()
            if r>=0.72: print(f'{g} 似ている {r:.2f}', x['key'], x['t'], '／', y.get('key','B'+str(y['n'])), y['t'])
print('ERROR',err)
