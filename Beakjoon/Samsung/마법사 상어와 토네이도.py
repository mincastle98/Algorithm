# G3
from copy import deepcopy
from pprint import pprint

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

now = (N // 2, N // 2)
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
spreaded = [[0, 0, 0.02, 0, 0],
            [0, 0.1, 0.07, 0.01, 0],
            [0.05, 0, 0, 0, 0],
            [0, 0.1, 0.07, 0.01, 0],
            [0, 0, 0.02, 0, 0]]


def rotate(degree):
    spreaded_ = [[0] * 5 for _ in range(5)]
    effected_zone = []
    if degree == 0:
        spreaded_ = deepcopy(spreaded)
        for r in range(5):
            for c in range(5):
                if spreaded[r][c]:
                    effected_zone.append([r, c])
    elif degree == 1:
        for r in range(5):
            for c in range(5):
                spreaded_[5 - c - 1][r] = spreaded[r][c]
                if spreaded_[5 - c - 1][r]:
                    effected_zone.append([5 - c - 1, r])
    elif degree == 2:
        for r in range(5):
            for c in range(5):
                spreaded_[5 - r - 1][5 - c - 1] = spreaded[r][c]
                if spreaded_[5 - r - 1][5 - c - 1]:
                    effected_zone.append([5 - r - 1, 5 - c - 1])
    elif degree == 3:
        for r in range(5):
            for c in range(5):
                spreaded_[c][5 - r - 1] = spreaded[r][c]
                if spreaded_[c][5 - r - 1]:
                    effected_zone.append([c, 5 - r - 1])

    return spreaded_, effected_zone


spreaded_by_dir = [rotate(0), rotate(1), rotate(2), rotate(3)]

di = 0
for i in range((N ** 2) - 1):
    now = [now[0] + dir[di][0], now[1] + dir[di][1]]

    # 모래 뿌리기
    remain_sand = board[now[0]][now[1]]
    spreaded_, effected_zone = spreaded_by_dir[di]
    for r, c in effected_zone:
        if spreaded_[r][c]:
            if 0 <= now[0] - (2 - r) < N and 0 <= now[1] - (2 - c) < N:
                board[now[0] - (2 - r)][now[1] - (2 - c)] += int(board[now[0]][now[1]] * spreaded_[r][c])
            else:
                answer += int(board[now[0]][now[1]] * spreaded_[r][c])
            remain_sand -= int(board[now[0]][now[1]] * spreaded_[r][c])

    if 0 <= now[0] + dir[di][0] < N and 0 <= now[1] + dir[di][1] < N:
        board[now[0] + dir[di][0]][now[1] + dir[di][1]] += remain_sand
    else:
        answer += remain_sand
    board[now[0]][now[1]] = 0
    pprint(board)
    print()
    if (now[0] <= N // 2 and now[0] - now[1] == 1) or (now[0] > N // 2 and now[0] == now[1]) or (
            now[0] + now[1] == N - 1):
        di = (di + 1) % 4

print(answer)
