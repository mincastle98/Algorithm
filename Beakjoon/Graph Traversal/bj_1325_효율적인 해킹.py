# 1325 - 효율적인 해킹
import sys

sys.setrecursionlimit(10 ** 6)

N, M = input().split()
N, M = int(N), int(M)

graph = {}
for i in range(N + 1):
    graph[i] = set()

for _ in range(M):
    a, b = input().split()
    graph[int(a)] |= {int(b)}
    graph[int(b)] |= {int(a)}

visited = [0 for _ in range(N + 1)]


def dfs(node):
    global linked
    linked += 1
    for v in graph[node]:
        if not visited[v]:
            dfs(v)


for i in range(N + 1):
    if not visited[i]:
        dfs(i)
        print(linked)
