# 9465 - 스티커(S1)
from copy import deepcopy


def check_axis(x, y):
    return x >= 0 and y >= 0 and x < n and y < 2


T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
    expectation = deepcopy(stickers)
    for i in range(2*n):
        x, y = i % n, i//n
        loss = 0
        for d in dir:
            if check_axis(x+d[1], y+d[0]):
                loss += stickers[y+d[0]][x+d[1]]
        expectation[y][x] -= loss

    for e in expectation:
        print(e)
