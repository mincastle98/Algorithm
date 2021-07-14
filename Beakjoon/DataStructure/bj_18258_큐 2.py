# 18258 - 큐 2
import sys
from collections import deque

N = int(sys.stdin.readline().strip())

queue = deque()
for _ in range(N):
    c = sys.stdin.readline().strip().split()

    if c[0] == "push":
        queue.append(int(c[1]))
    elif c[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif c[0] == "size":
        print(len(queue))
    elif c[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif c[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
