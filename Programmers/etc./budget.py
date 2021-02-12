# 예산
def solution(d, budget):
    answer = 0
    d.sort()

    for d_ in d:
        if budget - d_ >= 0:
            answer += 1
            budget -= d_

    return answer


print(solution([2, 2, 3, 3], 10))
