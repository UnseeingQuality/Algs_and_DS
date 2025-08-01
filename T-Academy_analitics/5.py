n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
best_pref = [[-10**11 for _ in range(n+1)] for _ in range(k+1)]

for i in range(0, k+1):
    best_pref[i][0] = dp[i][0]

for i in range(k+1):
    dp[i][1] = a[0] # на первую ступеньку можно встать единст обр-м
    best_pref[i][1] = max(best_pref[i][0], dp[i][1])

    if n >= 2:
        dp[i][2] = max(a[0], 0) + a[1]
        best_pref[i][2] = max(best_pref[i][1], dp[i][2])


for i in range(3, n+1): # честно прогоним цикл для попытки без абстракций
    dp[0][i] = max(dp[0][i-2], dp[0][i-1]) + a[i-1]
    best_pref[0][i] = max(best_pref[0][i - 1], dp[0][i])

for i in range(1,k+1):
    for j in range(3,n+1):
        val_step = max(dp[i][j-1], dp[i][j-2])
        val_telep = best_pref[i-1][j-1]
        dp[i][j] = max(val_telep, val_step) + a[j-1]
        best_pref[i][j] = max(best_pref[i][j - 1], dp[i][j])

res = max([dp[i][n] for i in range(0, k+1)])
print(res)

