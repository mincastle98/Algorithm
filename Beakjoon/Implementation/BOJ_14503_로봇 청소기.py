# 14503 - 로봇 청소기(G5)
N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
now = [r, c]

d = (d + 2) % 4 if d % 2 == 1 else d
dir = ((-1, 0), (0, -1), (1, 0), (0, 1))
answer = 0

stop_flag = False
while not stop_flag:
    if board[now[0]][now[1]] == 0:
        board[now[0]][now[1]] = 2
        answer += 1
    isCleanable = False
    for i in range(1, 5):
        dxdy = dir[(d + i) % 4]
        if board[now[0] + dxdy[0]][now[1] + dxdy[1]] == 0:
            d = (d + i) % 4
            now = [now[0] + dxdy[0], now[1] + dxdy[1]]
            isCleanable = True
            break

    if not isCleanable:
        now = [now[0] - dir[d][0], now[1] - dir[d][1]]
        if board[now[0]][now[1]] == 1:
            stop_flag = True

print(answer)
