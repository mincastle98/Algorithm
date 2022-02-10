# 11286 - 절댓값 힙(S1)
import sys
import heapq

N = int(input())

ops = []
for _ in range(N):
    ops.append(int(sys.stdin.readline()))

max_heap = []
for op in ops:
    if op:
        heapq.heappush(max_heap, (abs(op), op))
    else:
        try:
            abs_mins = [heapq.heappop(max_heap)[1]]
            while max_heap and abs_mins[-1] > 0 and max_heap[0][1] == abs_mins[0]:
                abs_mins.append(heapq.heappop(max_heap)[1])

            flag = False
            i = 0
            while i < len(abs_mins) and abs_mins[i] > 0:
                i += 1
            i -= 1
            print(abs_mins[i])
            abs_mins.pop(i)

            for min in abs_mins:
                heapq.heappush(max_heap, (abs(min), min))
        except:
            print(0)
