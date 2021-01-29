from itertools import combinations


def solution(numbers):
    comb = list(combinations(numbers, 2))

    sumList = [i[0] + i[1] for i in comb]
    sumList = list(set(sumList))
    sumList.sort()

    answer = sumList
    return answer
