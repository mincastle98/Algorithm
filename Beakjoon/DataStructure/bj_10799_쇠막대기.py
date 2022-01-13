# 10799 - 쇠막대기
sticks = input()

stack = []
ans = 0
idx = 0
while idx < len(sticks):
    if sticks[idx] == '(':
        stack.append(sticks[idx])
        if sticks[idx+1] == ')':
            idx += 1
            stack.pop()
            ans += len(stack)
    else:
        stack.pop()
        ans += 1

    idx += 1

print(ans)
