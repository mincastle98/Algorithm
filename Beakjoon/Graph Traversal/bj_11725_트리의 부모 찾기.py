# 11725 - 트리의 부모 찾기
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = input().split()
    graph[int(a)] |= {int(b)}
    graph[int(b)] |= {int(a)}

visited = [0 for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]


def dfs(node):
    for v in graph[node]:
        if parent[node] == v: continue
        parent[v] = node
        if not visited[v]:
            dfs(v)


dfs(1)
for i in range(2, N + 1):
    print(parent[i])
