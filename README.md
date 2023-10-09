# ここどこ

テキストの処理についてPythonで勉強するリポジトリ

TODO
- [x] 編集距離
- [x] wuの差分検出アルゴリズム
- 転置index
- ベクトル化
- テキストマイニング?

# wuの差分検出アルゴリズム

githubのdiffで見れるような、挿入と削除と変更の差分を取得する方法が知りたい

平均計算量がO(N+PD)で、最悪計算量がO(NP)。ここでNは二つの文字列の長さの和で、PはSESにおける削除の合計数。Dは編集距離

参考資料
- [https://gihyo.jp/dev/column/01/prog/2011/diff_sd200906](https://gihyo.jp/dev/column/01/prog/2011/diff_sd200906)
- [https://qiita.com/convto/items/e05d8147d9808a27b8ff](https://qiita.com/convto/items/e05d8147d9808a27b8ff)
- []

### 考え方

エディットグラフという、二つの文字列を縦横の軸において、各文字列の文字を碁盤のように並べたもの。縦横の番地が文字列の各要素になるイメージ

ここで追加をy軸方向+1、削除をx軸方向+1、同じ要素だったらxとy両方に+1（つまり斜め移動）というように定義。  
二つの文字列の長さがM,Nの時、0,0の点からM,Nの点までの最短経路を求める問題として考えられる（これは編集距離を解く時にも出てくる考え）

この時愚直に全探索するとO(MN)かかるのと、メモリがもったいない  

そのため、二つの文字列の長さをM,N(N>=M)として、N-Mを$\Delta$とする  
また先述の通り編集距離はDで、SESにおける削除の合計数をPとしたとき、Dを以下の式で求める
$$
D = \Delta + 2P
$$

ここで$\Delta$が、二つの文字列の長さだけわかっているときの最小の編集距離。例えばabcとabcdeという文字列だった時、5-3で2が最小の編集距離だね～ということ  
片方の文字列が二つの文字列のLCSに完全に一致するときの編集距離はそのまま$\Delta$が該当する

y軸に$\Delta$だけ進んでから対角線上に進むと編集距離が$\Delta$になる。  
そうじゃない場合は対角線の上か下を通る。この時P分対角線から移動すると、対角線に戻るのに再びPかかるので、結果として上記の式のように2Pが出てくる

wuのアルゴリズムでは探索範囲をy軸に$\Delta+P+1$、x軸に$P+1$の範囲に絞っている

## 実装

対角線kを$y-x$として定義

$-P <= k  <= \Delta+P$ を探索範囲として、P=pの場合の各対角線k上における、到達可能な点をfp(k,p)  
任意の点(x,y)から到達可能な最遠点fp(k,p)を計算する関数をsnake(k,y)と定義する

この対角線kをスライドして探索しつつ、斜めにどこまで進めるか調べてく感じっぽい  
まだeditグラフのy(横方向)は、長い方の文字列になる

実際pはわからんため、ちょっとずつ値を動かして探索していく。差分が少ないと計算量も少ないが、一方差分がでかすぎると結構重いらしい

$\Delta$は、文字列の長さが取得できたタイミングで確定するので、あとは最小のpを探す  
Pが取りうる複数のkで、最も遠い点を探して、この時M,Nの点が含まれていれば、その時の編集距離からDが求まる

### fpの実装

斜めにいつまで移動できるかを調べるので、xとyを一緒にインクリメントしてそのcharを比較すればよい  
この時yを返せば、x = y - kでxが求まるので、xは不要、らしい

k+1とk-1の最遠点を調べて、そこからkに近づけて最遠点を調べて、という感じっぽい

- kが-pから$\Delta$-1の範囲の時
- kが$\Delta$の時
- kが$\Delta$+1から$\Delta$+pの範囲の時

で計算が変わる


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
