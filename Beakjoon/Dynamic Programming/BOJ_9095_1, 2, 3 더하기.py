# 9095 - 1, 2, 3 더하기(S3)
T = int(input())
testcases = [int(input()) for _ in range(T)]
for t in range(T):
    dp = [1, 1, 2, 4]
    n = testcases[t]
    for i in range(4, n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])

    print(dp[n])
