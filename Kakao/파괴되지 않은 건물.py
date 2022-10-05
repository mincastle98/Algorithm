# 2022 KAKAO BLIND RECRUITMENT - 파괴되지 않은 건물(Level 3)
def solution(board, skill):
    answer = 0

    skill_sum = [[0] * (len(board[0]) + 2) for _ in range((len(board) + 2))]

    for s in skill:
        degree = -s[5] if s[0] == 1 else s[5]
        skill_sum[s[1] + 1][s[2] + 1] += degree
        skill_sum[s[1] + 1][s[4] + 2] += -degree
        skill_sum[s[3] + 2][s[2] + 1] += -degree
        skill_sum[s[3] + 2][s[4] + 2] += degree

    for i in range(1, len(skill_sum)):
        for j in range(1, len(skill_sum[0])):
            skill_sum[i][j] += skill_sum[i - 1][j] + skill_sum[i][j - 1] - skill_sum[i - 1][j - 1]
            if i < (len(board) + 1) and j < (len(board[0])) + 1 and board[i - 1][j - 1] + skill_sum[i][j] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
