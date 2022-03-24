# 1890 - 점프(S2)
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        for k in range(1, 10):
            if i < k and j < k:
                break
            if j-k >= 0 and board[i][j-k] == k:
                dp[i][j] += dp[i][j-k]
            if i-k >= 0 and board[i-k][j] == k:
                dp[i][j] += dp[i-k][j]

print(dp[-1][-1])
