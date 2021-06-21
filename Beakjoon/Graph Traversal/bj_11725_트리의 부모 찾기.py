from collections import deque

N = int(input())
graph = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = input().split()
    graph[int(a)] |= {int(b)}
    graph[int(b)] |= {int(a)}

queue = deque()
queue.append(1)
visited = [0 for _ in range(N + 1)]
visited[1] = 1
while queue:
    node = queue.popleft()
    if visited[node]: continue
    for i in graph[node]:
        if not visited[i]:
            queue.append(i)
            visited[i] = node

for i in range(2, N + 1):
    print(visited[i])
