# 1969 - DNA(S5)
import sys

N, M = list(map(int, sys.stdin.readline().split()))
dna = sys.stdin.readline()
strings = []
for _ in range(N):
    strings.append(sys.stdin.readline())

answer = 0
for string in strings:
    tmp = 0
    for i in range(M):
        if string[i] != dna[i]:
            tmp += 1
    if tmp > answer:
        answer = tmp

print(answer)
