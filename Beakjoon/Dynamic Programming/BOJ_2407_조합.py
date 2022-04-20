# 2407 - 조합(S3)
n, m = map(int, input().split())

dp = [1]
for i in range(1, n+1):
    dp.append(dp[-1]*i)


print(dp[n]//(dp[n-m]*dp[m]))
