# 소수 구하기
from math import sqrt


def solution(m, n):
    for i in range(m, n + 1):
        flag = 1
        if i == 2:
            print(i)
        elif not i & 1 or i == 1:
            continue
        else:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    flag = 0
                    break
            if flag:
                print(i)


inputs = list(map(int, input().split(" ")))
solution(inputs[0], inputs[1])
