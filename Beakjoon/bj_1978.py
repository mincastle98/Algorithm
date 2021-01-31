from math import sqrt


def solution(num):
    answer = 0
    for i in num:
        flag = 1

        if i == 1:
            continue
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                flag = 0
                break

        if flag:
            answer += 1

    print(answer)


n = int(input())
inputs = list(map(int, input().split(" ")))
inputs = inputs[:n]
solution(inputs)
