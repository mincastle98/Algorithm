# N과 M(1)

def solution(N, M):
    stack = [i for i in range(N, 0, -1)]
    answer = []
    node = []

    while stack:
        flag = 0
        node.append(stack.pop())
        for i in range(N):
            if not i + 1 in answer or i + 1 != node:
                stack.append(i + 1)
                flag = 1

        if flag:
            answer.append(node)
        else:
            answer.pop()

        if

    return 0


N, M = map(int, (input().split()))
solution(N, M)
