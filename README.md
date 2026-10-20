# 振り返りジャーナル テーマ選び

小学校高学年向けの振り返りジャーナル用テーマ200本を、検索・絞り込み・ランダムで選ぶ先生用ツール。
★お気に入り・使った記録・追加テーマはブラウザの中（localStorage）に保存されます。

公開URL: https://kawaitomohiro.github.io/journal-themes/

## 作り直し方
- 画面のひな形: `src/app.html`（テーマの差しこみ位置は `/*__BUILTIN__*/`）
- テーマの元: `data_src/original.html`（元の HTML。200テーマの配列を取り出して使う）
- `python3 build.py` で `index.html` を作る → `git push` で公開に反映
