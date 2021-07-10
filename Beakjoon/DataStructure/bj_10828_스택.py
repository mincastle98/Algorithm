# 10828 - 스택
import sys

N = int(sys.stdin.readline().strip())

stack = []
for _ in range(N):
    c = sys.stdin.readline().strip().split()

    if c[0] == "push":
        stack.append(int(c[1]))
    elif c[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c[0] == "size":
        print(len(stack))
    elif c[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif c[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
