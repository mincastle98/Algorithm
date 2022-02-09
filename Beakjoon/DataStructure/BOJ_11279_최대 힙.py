# 11279 - 최대 힙(S2)
import sys
import heapq

N = int(input())

ops = []
for _ in range(N):
    ops.append(int(sys.stdin.readline()))

max_heap = []
for op in ops:
    if op:
        heapq.heappush(max_heap, -op)
    else:
        try:
            print(-heapq.heappop(max_heap))
        except:
            print(0)
