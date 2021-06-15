import sys
sys.setrecursionlimit(10 ** 6)

N, M, V = input().split()
N, M, V = int(N), int(M), int(V)
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = input().split()
    graph[int(a) - 1][int(b) - 1] = 1
    graph[int(b) - 1][int(a) - 1] = 1


def dfs(node):
    visited.append(node)
    for i in range(N):
        if graph[node][i] and i not in visited:
            dfs(i)


visited = []
dfs(V - 1)
for i in visited:
    print(i + 1, end=' ')
print("")


def bfs(node):
    for i in range(N):
        if graph[node][i] and i not in visited and i not in queue:
            visited.append(i)
            queue.append(i)
    if queue:
        bfs(queue.pop(0))


visited = [V - 1]
queue = []
bfs(V - 1)
for i in visited:
    print(i + 1, end=' ')
