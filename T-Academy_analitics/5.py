n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = a[0] # на первую ступеньку можно встать единст обр-м

if n >= 2:
    dp[1] = max(a[0], 0) + a[1]

for i in range(2, n + 1):
    dp[i] = max(dp[i-2], dp[i-1]) + a[i]



