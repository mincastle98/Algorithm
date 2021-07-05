# 1325 - 효율적인 해킹
N, M = input().split()
N, M = int(N), int(M)

graph = {}
for i in range(N + 1):
    graph[i] = set()

for _ in range(M):
    a, b = input().split()
    graph[int(b)] |= {int(a)}

linked = []

for i in range(1, N + 1):
    stack = [i]
    visited = [0 for _ in range(N + 1)]
    temp = []
    while stack:
        now = stack.pop()
        for j in graph[now]:
            if not visited[j]:
                visited[j] = 1
                stack.append(j)
                temp.append(j)

    if linked:
        if len(linked[-1][1]) < len(temp):
            linked.clear()
            linked.append([i, temp])
        elif len(linked[-1][1]) == len(temp):
            linked.append([i, temp])
    else:
        linked.append([i, temp])

for i in linked:
    print(i[0], end=' ')
