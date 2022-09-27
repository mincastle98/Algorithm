# 정수 삼각형(Level 3)
def solution(triangle):

    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0] = [triangle[0][0]]

    for h in range(1, len(triangle)):
        for idx, node in enumerate(triangle[h]):
            if idx > 0:
                dp[h][idx] = max(dp[h][idx], dp[h - 1][idx - 1] + triangle[h][idx])
            if idx < len(triangle[h]) - 1:
                dp[h][idx] = max(dp[h][idx], dp[h - 1][idx] + triangle[h][idx])

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
