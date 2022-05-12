# 1912 - 연속합(S2)
n = int(input())
arr = list(map(int, input().split()))

dp = arr[:]

for i in range(1, n):
    if dp[i - 1] + dp[i] > dp[i]:
        dp[i] += dp[i - 1]

print(max(dp))
