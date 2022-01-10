# 10866 - 덱
N = int(input())
commands = []
for _ in range(N):
    commands.append(input().split())

deque = [0] * N
head = 0
tail = 0

for command in commands:
    if command[0] == "push_front":
        deque[head] = command[1]
        head = (head-1) % len(deque)
    elif command[0] == "push_back":
        tail = (tail+1) % len(deque)
        deque[tail] = command[1]
    elif command[0] == "pop_front":
        if head == tail:
            print(-1)
        else:
            head = (head+1) % len(deque)
            print(deque[head])
    elif command[0] == "pop_back":
        if head == tail:
            print(-1)
        else:
            print(deque[tail])
            tail = (tail-1) % len(deque)
    elif command[0] == "size":
        if tail >= head:
            print(tail-head)
        else:
            print(len(deque)-head+tail)
    elif command[0] == "empty":
        print(1 if head == tail else 0)
    elif command[0] == "front":
        if head == tail:
            print(-1)
        else:
            print(deque[(head+1) % len(deque)])
    elif command[0] == "back":
        if head == tail:
            print(-1)
        else:
            print(deque[tail])
