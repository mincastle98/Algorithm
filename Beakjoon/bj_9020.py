# 골드바흐의 추측
from math import sqrt

MAX = 10000


def solution(numList):
    primes = [False, False] + [True] * (MAX - 1)

    for i in range(2, int(sqrt(MAX)) + 1):
        if primes[i]:
            for j in range(2 * i, MAX + 1, i):
                primes[j] = False

    for num in numList:
        for i in range(num // 2, 1, -1):
            if primes[i] and primes[num - i]:
                print(i, num - i)
                break


n = int(input())
inputList = []
for i in range(n):
    inputList.append(int(input()))

solution(inputList)
