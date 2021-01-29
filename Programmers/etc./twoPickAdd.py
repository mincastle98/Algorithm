from itertools import combinations


def solution(numbers):
    answer = [i[0] + i[1] for i in list(combinations(numbers, 2))]
    answer = list(set(answer))
    answer.sort()

    return answer


solution([5, 0, 2, 7])
