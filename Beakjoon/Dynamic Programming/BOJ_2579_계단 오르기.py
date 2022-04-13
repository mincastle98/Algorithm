# 2579 - 계단 오르기(S3)
n = int(input())
stairs = [int(input()) for _ in range(n)]

if n == 1:
    print(stairs[0])
else:
    dp = [0, stairs[0], stairs[0]+stairs[1]]

    for i in range(3, n+1):
        tmp = max(dp[-2], dp[-3]+stairs[i-2])
        dp.append(tmp+stairs[i-1])

    print(dp[n])
