N = int(input())
dp = [0, 0]

for i in range(2, N+1):
    tmp = dp[i-1]
    if i % 2 == 0:
        tmp = min(tmp, dp[i//2])
    if i % 3 == 0:
        tmp = min(tmp, dp[i//3])
    dp.append(tmp+1)

print(dp[-1])
