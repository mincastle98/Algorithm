import math


def solution():
    num = input()
    list = dict()

    for i in str(num):
        if i in list:
            list[i] += 1
        else: list[i] = 1

    tmp = 0
    max = 0
    for i in list:
        if i == '6' or i == '9':
            tmp += list[i]
        elif list[i] > max:
            max = list[i]

    if math.ceil(tmp/2) > max:
        answer = math.ceil(tmp/2)
    else: answer = max

    print(answer)


solution()