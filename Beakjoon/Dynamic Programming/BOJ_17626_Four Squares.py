# 17626 - Four Squares(S4)
import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    for j in range(int(i**0.5), 0, -1):
        dp[i] = min(dp[i], dp[i-j*j]+1)
        if dp[i] == 1:
            break

print(dp[-1])
