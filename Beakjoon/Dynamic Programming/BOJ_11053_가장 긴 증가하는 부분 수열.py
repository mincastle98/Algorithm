# 11053 - 가장 긴 증가하는 부분 수열(S2)
N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
dp[-1] = 1

for i in range(N-2, -1, -1):
    if A[i] < A[i+1]:
        dp[i] = dp[i+1]+1
    else:
        dp[i] = dp[i+1]

print(dp[0])
