n = int(input())
dp = [[0,0] for i in range(n+1)]

dp[1] = [1,1] # [0] - колво башен с синим концом, [1] - с красным
dp[2] = [2, 1]

for i in range(3, n+1):
    dp[i][1] = dp[i-1][0]
    dp[i][0] = dp[i-1][1] + dp[i-1][0]

print(sum(dp[n]))