# 2839 - 설탕배달(B1)
import math
import sys

N = int(sys.stdin.readline())

dp = [math.inf, math.inf, math.inf, 1, math.inf, 1]
for i in range(6, N+1):
    tmp = min(dp[i-3], dp[i-5])
    dp.append(tmp+1)

print(dp[N] if dp[N] != math.inf else -1)
