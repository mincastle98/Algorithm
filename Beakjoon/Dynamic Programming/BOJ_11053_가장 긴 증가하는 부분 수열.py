# 11053 - 가장 긴 증가하는 부분 수열(S2)
N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
print(dp)
