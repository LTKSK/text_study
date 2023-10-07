# 開始位置、k,yを渡すと、斜めに進めるだけ進んで、進めなくなった地点のyを返す
def snake(a, b, m, n, k, y) -> int:
    x = y - k
    while x < m and y < n and a[x] == b[y]:
        x += 1
        y += 1
    return y

def wu(a, b):
    m = len(a)
    n = len(b)
    # mのほうが大きい必要がある
    m, n = (m, n) if m > n else (n, m)
    delta = m-n
    offset = m + 1
    fp = [0] * (m+n+3)

    for p in range(0, m + n + 1):
        for k in range(-p, delta):
            fp[k + offset] = snake(a, b, m, n, k, max(fp[k - 1 + offset] + 1, fp[k + 1 + offset]))

        for k in range(delta + p, delta, -1):
            fp[k + offset] = snake(a, b, m, n, k, max(fp[k - 1 + offset] + 1, fp[k + 1 + offset]))

        fp[delta + offset] = snake(a, b, m, n, delta, max(fp[delta - 1 + offset] + 1, fp[delta + 1 + offset]))

        if fp[delta + offset] == n:
            return delta + 2 * p


s1 = 'abcdefg'
s2 = 'adfg'


print(wu(s1, s2))
