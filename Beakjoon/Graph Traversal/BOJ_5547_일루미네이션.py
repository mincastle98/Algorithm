# 5547 - 일루미네이션(G5)
import sys
sys.setrecursionlimit(1000000)

W, H = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

dxdy_odd = [(1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (1, -1)]
dxdy_even = [(1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

groups = []
visited = [[0]*W for _ in range(H)]


def check_axis(x, y):
    return x >= 0 and y >= 0 and x < W and y < H


def dfs(x, y, type):
    tmp = []
    if check_axis(x, y) and board[y][x] == type and not visited[y][x]:
        visited[y][x] = 1
        tmp += [(x, y)]
        dxdy = dxdy_odd if y % 2 == 0 else dxdy_even
        for i in range(len(dxdy)):
            tmp += dfs(x+dxdy[i][0], y+dxdy[i][1], type)

    return tmp


def get_border(arr, type):
    border = 0
    for x, y in arr:
        dxdy = dxdy_odd if y % 2 == 0 else dxdy_even
        for i in range(6):
            if not check_axis(x+dxdy[i][0], y+dxdy[i][1]) or board[y+dxdy[i][1]][x+dxdy[i][0]] != type:
                border += 1

    return border


def is_outer_border(arr):
    if 0 in list(map(lambda x: x[0], arr)):
        return True
    elif 0 in list(map(lambda x: x[1], arr)):
        return True
    elif W-1 in list(map(lambda x: x[0], arr)):
        return True
    elif H-1 in list(map(lambda x: x[1], arr)):
        return True
    else:
        return False


answer = 0
for x in range(W):
    for y in range(H):
        if not visited[y][x]:
            tmp = dfs(x, y, board[y][x])

            if board[y][x]:
                answer += get_border(tmp, 1)
            else:
                if not is_outer_border(tmp):
                    answer -= get_border(tmp, 0)

print(answer)
