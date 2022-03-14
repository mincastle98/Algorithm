def solution(width, height, diagonals):
    answer = 0

    diagonal_points = []
    for x, y in diagonals:
        diagonal_points.append(((x-1, y), (x, y-1)))
        diagonal_points.append(((x, y-1), (x-1, y)))

    for point in diagonal_points:
        dp = [[1]*(point[0][0]+1) for _ in range(point[0][1]+1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        dp2 = [[1]*(width - point[1][0]+1)
               for _ in range(height-point[1][1]+1)]
        for i in range(1, len(dp2)):
            for j in range(1, len(dp2[i])):
                dp2[i][j] = dp2[i-1][j] + dp2[i][j-1]
        answer += dp[-1][-1] * dp2[-1][-1]

    return answer % 10000019


print(solution(51, 37, [[17, 19]]))
