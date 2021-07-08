# 1158 - 요세푸스 문제
N, K = map(int, input().split())

li = [i for i in range(1, N + 1)]

print("<", end='')

target = 1
while li:
    if target == 0: target = 1
    target = (target + K - 1) % len(li)
    print(li[target - 1], end='')
    li.pop(target - 1)
    if li: print(", ", end='')

print(">", end='')
