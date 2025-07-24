def bodyswap(a,b):
    print(a,b)
    body[a],body[b] = body[b],body[a]
    return body[b]

n, swaps_cnt = list(map(int, input().split())) # кол-во героев и кол-во обменов
body = [0] * (n + 1)
for i in range(n+1):
    body[i] = i
# начальные обмены
for i in range(swaps_cnt):
    a,b = map(int, input().split())
    body[a], body[b] = body[b], body[a]

for i in range(1, n-1):
    if body[i] != i:
        now = i
        while body[now] != i:
            now = bodyswap(now, n - 1)
        now = bodyswap(now, n)
        now = bodyswap(now, n)
        bodyswap(body[n - 1], n - 1)

if body[n-1] == n:
    bodyswap(n, n - 1)