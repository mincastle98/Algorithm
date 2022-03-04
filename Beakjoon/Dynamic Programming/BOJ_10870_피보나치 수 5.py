# 10870 - 피보나치 수 5(B2)
import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
if n > 0:
    dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[-1])
