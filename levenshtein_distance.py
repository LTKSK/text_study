def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)

    dp = [[0] * (n+1) for _ in range(m+1)]


    # dpのテーブル初期化
    # tableの縦と横のコストは、文字列を1文字ずつ削除するという操作をした時のコストになっている
    # 要するに空文字列との編集距離
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            # 同じ文字の時は0それ以外は、何かしらの修正を行う
            edit_cost = 0 if s1[i-1] == s2[j-1] else 1
            # 今回の例では挿入も削除も同じコストなのでどっちも1
            dp[i][j] = min(
                dp[i-1][j] + 1, # 挿入
                dp[i][j-1] + 1, # 削除
                dp[i-1][j-1] + edit_cost) # 置き換え
    return dp[m][n]
