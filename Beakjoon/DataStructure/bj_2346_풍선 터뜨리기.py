# 2346 - 풍선 터뜨리기
from collections import deque
N = int(input())
ballons = deque(
    list(map(lambda x, y: (int(x), y), input().split(), [i+1 for i in range(N)])))

now = ballons.popleft()
for _ in range(N-1):
    print(now[1], end=" ")
    if now[0] > 0:
        for _ in range((now[0] - 1) % len(ballons)):
            ballons.append(ballons.popleft())
    elif now[0] < 0:
        for _ in range(now[0]*(-1) % len(ballons)):
            ballons.appendleft(ballons.pop())

    now = ballons.popleft()

print(now[1], end="")
