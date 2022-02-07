# 약수의 개수와 덧셈
import math


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, int(math.sqrt(i))):
            if i % j == 0:
                cnt += 1
        cnt *= 2
        if int(math.sqrt(i)) == math.sqrt(i):
            cnt += 1

        if cnt & 1:
            answer -= i
        else:
            answer += i

    return answer
