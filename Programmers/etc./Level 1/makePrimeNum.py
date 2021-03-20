# 소수 만들기
from itertools import combinations
import math


def solution(nums):
    answer = 0
    combList = list(combinations(nums, 3))
    for c in combList:
        tmp = sum(c)
        flag = True
        for i in range(2, math.floor(math.sqrt(tmp)) + 1):
            if not tmp % i:
                flag = False
                break
        if flag:
            answer += 1

    return answer


print(solution([1, 2, 7, 6, 4]))
