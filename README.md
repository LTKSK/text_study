# ここどこ

テキストの処理についてPythonで勉強するリポジトリ

TODO
- [x] 編集距離
- [ ] wuの差分検出アルゴリズム
- 転置index
- ベクトル化
- テキストマイニング?

## wuの差分検出アルゴリズム

githubのdiffで見れるような、挿入と削除と変更の差分を取得する方法が知りたい

参考資料
- [https://gihyo.jp/dev/column/01/prog/2011/diff_sd200906](https://gihyo.jp/dev/column/01/prog/2011/diff_sd200906)
- [https://qiita.com/convto/items/e05d8147d9808a27b8ff](https://qiita.com/convto/items/e05d8147d9808a27b8ff)
- []

### 単語

- LCS
  - Longest Common Subsequence
  - 文字列AとBがあるとき、それらの最長共通部分列
  - 最長共通部分列ってなんだよ...
    - 文字列AとBがあるとき、共通する部分で最も長い列のこと
      - 複数存在しうる
    - 参考資料にあるけど、abcdefとdacfeaの共通の文字はa,c,d,e,fの五つ
      - ここでLCSはacf
        - `a`b`c`de`f`とd`acf`eaということ。dはどちらにも含まれるけど、順序通りに並ばないのでなし。上の例だと、aceもLCSに該当する
- SES
  - Shortest Edit Script
  - 文字列AとBがあるとき、それらの間を埋めるための挿入、削除の最短手順のこと
    - 片方をもう片方と同じ文字列にするために必要な編集作業の数
- Edit Distance
  - または編集距離とか、レーベンシュタイン距離とか
  - SESの挿入と削除の回数の合計