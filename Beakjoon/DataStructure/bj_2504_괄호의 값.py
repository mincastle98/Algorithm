# 2504 - 괄호의 값
brackets = input()

stack = []

for bracket in brackets:
    if bracket in ['(', '[']:
        stack.append(bracket)
    elif not stack:
        print(0)
        exit(0)
    elif bracket == ')':
        idx = -1
        while str(stack[idx]).isdigit() and idx*(-1) < len(stack):
            idx -= 1
        if stack[idx] == '(':
            if idx == -1:
                result = 1
            else:
                result = sum(stack[idx+1:])
            stack = stack[:idx]
            stack.append(2*result)
        else:
            print(0)
            exit(0)
    elif bracket == ']':
        idx = -1
        while str(stack[idx]).isdigit() and idx*(-1) < len(stack):
            idx -= 1
        if stack[idx] == '[':
            if idx == -1:
                result = 1
            else:
                result = sum(stack[idx+1:])
            stack = stack[:idx]
            stack.append(3*result)
        else:
            print(0)
            exit(0)
    else:
        stack = [0]
        break

if '(' in stack or '[' in stack:
    print(0)
    exit(0)
else:
    print(sum(stack))
