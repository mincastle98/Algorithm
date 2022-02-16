# 22942 - 데이터 체커(G4)
import sys

N = int(input())
boundarys = []
for i in range(N):
    center, radius = list(map(int, sys.stdin.readline().split()))
    boundarys.append((center-radius, i))
    boundarys.append((center+radius, i))
boundarys.sort()

stack = []
for boundary in boundarys:
    if not stack:
        stack.append(boundary)
    else:
        if stack[-1][0] == boundary[0]:
            print("NO")
            exit(0)
        elif stack[-1][1] == boundary[1]:
            stack.pop()
        else:
            stack.append(boundary)

if stack:
    print("NO")
else:
    print("YES")
