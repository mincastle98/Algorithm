# 1966 - 프린터 큐
import heapq
from collections import deque

testcase = int(input())

ans_list = []
for _ in range(testcase):
    N, for_print = list(map(int, input().split()))
    docs = list(map(int, input().split()))

    printer = deque()
    for idx, doc in enumerate(docs):
        printer.append((doc, idx))

    maxHeap = list(map(lambda x: x[0] * (-1), printer))
    heapq.heapify(maxHeap)

    ans = (-1, -1)
    while ans[1] != for_print:
        now = heapq.heappop(maxHeap) * (-1)

        first = printer.popleft()
        while first[0] != now:
            printer.append(first)
            first = printer.popleft()

        ans = first
    ans_list.append(N-len(printer))

for ans in ans_list:
    print(ans)
