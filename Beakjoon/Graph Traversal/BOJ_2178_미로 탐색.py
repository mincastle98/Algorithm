# 2178 - 미로 탐색(S1)
N, M = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def check_axis(y, x):
    return y >= 0 and y < N and x >= 0 and x < M


def dfs(y, x):
    if (y, x) == (N-1, M-1):
        return 1
    elif not check_axis(y, x) or maze[y][x] == 0 or visited[y][x]:
        return N*M
    else:
        visited[y][x] = 1
        min_route = N*M
        for dy, dx in dir:
            min_route = min(dfs(y+dy, x+dx)+1, min_route)
        return min_route


print(dfs(0, 0))
