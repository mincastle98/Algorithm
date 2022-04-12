# 2579 - 계단 오르기(S3)
n = int(input())
stairs = [int(input()) for i in range(n)]

dp = [(0, 0), (stairs[0], 0), (stairs[0]+stairs[1], 1)]

for i in range(3, n+1):
    tmp = max(dp[i-1][0] if dp[i-1][1] == 0 else 0, dp[i-2][0])
    jump_cnt = 1 if tmp == dp[i-1][0] else 0
    dp.append((tmp+stairs[i-1], jump_cnt))

print(dp)
