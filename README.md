# 振り返りジャーナル テーマ選び

小学校1〜6年の振り返りジャーナル用テーマ400本（低学年100・中学年100・高学年200）を、検索・絞り込み・ランダムで選ぶ先生用ツール。
★お気に入り・使った記録・追加テーマはブラウザの中（localStorage）に保存されます。

公開URL: https://kawaitomohiro.github.io/journal-themes/

## 作り直し方
- 画面のひな形: `src/app.html`（テーマの差しこみ位置は `/*__BUILTIN__*/`）
- 高学年200の元: `data_src/original.html`（元の HTML から配列を取り出す）
- 低学年100・中学年100: `data_src/themes_low_mid.py`（「問い | ねらい | タグ | 時期 | 段階」の1行1テーマ。設計の根拠は冒頭のコメント）
- `python3 build.py` で `index.html` を作る → `git push` で公開に反映
