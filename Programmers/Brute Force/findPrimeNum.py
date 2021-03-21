# 소수 찾기
import math
from itertools import permutations


def solution(numbers):
    answer = 0
    permList = set()
    for l in range(1, len(numbers) + 1):
        permList |= set(permutations(list(numbers), l))
    permList = list(permList)
    permList_ = set()
    for c in permList:
        tmp = int("".join(c))
        permList_ |= {tmp}

    for c in permList_:
        flag = True
        if c < 2: continue
        for i in range(2, int(math.sqrt(c)) + 1):
            if not c % i:
                flag = False
                break
        if flag:
            answer += 1

    return answer


print(solution("011"))
