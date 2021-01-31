# 베르트랑 공준
from math import sqrt

MAX = 123456


def solution(numList):
    primes = [(0 if i & 1 else -1) for i in range(2 * MAX + 1)]
    primes[1] = -1
    primes[2] = 1

    for n in numList:
        if n == 0: break

        cnt = 0
        for i in range(n + 1, 2 * n + 1):
            if primes[i] == 1:
                cnt += 1
            elif not primes[i]:
                for j in range(2, int(sqrt(i)) + 1):
                    if i % j == 0:
                        primes[i] = -1
                        break
                if not primes[i]:
                    primes[i] = 1
                    cnt += 1

        print(cnt)


inputFlag = 1
inputs = []
while inputFlag:
    tmp = int(input())
    inputs.append(tmp)
    if not tmp:
        inputFlag = 0

solution(inputs)
