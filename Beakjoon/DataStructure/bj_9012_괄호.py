# 9012 - 괄호
N = int(input())

ps = []
for _ in range(N):
    ps.append(input())

for p in ps:
    stack = []
    flag = 1
    for pp in p:
        if pp == '(':
            stack.append('(')
        elif pp == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break

    if stack: flag = 0

    if flag:
        print("YES")
    else:
        print("NO")
