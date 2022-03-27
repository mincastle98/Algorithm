# 14503 - 로봇 청소기(G5)
def check_axis(y, x):
    return y >= 0 and x >= 0 and y < N and x < M


def check_cleanable(y, x, d):
    for i in range(4):
        next_d = (d-i+4) % 4
        next_x, next_y = y+dir[next_d][0], x+dir[next_d][1]
        if board[next_y][next_x] == 0 and not visited[next_y][next_x]:
            return next_y, next_x, next_d
    return 0, 0, -1


N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))

answer = 0
stack = [(r, c, d)]
false_flag = 0
while stack:
    y, x, d = stack.pop()
    if check_axis(y, x) and board[y][x] == 0 and not visited[y][x]:  # 청소 가능
        false_flag = 0
        visited[y][x] = 1
        answer += 1
        next_y, next_y, next_d = check_cleanable(y, x, d)
        if next_d != -1:
            stack(next_y, next_y, next_d)

    else:   # 청소 불가능
        if board[y-dir[d][0]][x-dir[d][1]] == 0:
            stack.append((y-dir[d][0], x-dir[d][1], d))
            false_flag += 1
            if false_flag == 4:
                break

for v in visited:
    print(v)
print(answer)
