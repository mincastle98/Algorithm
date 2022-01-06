# 1918 - 후위 표기식
expression = input()

expression = list(expression)
op_stack = []
priority = {'+': 1, '-': 1, '*': 2, '/': 2}

for e in expression:
    if e not in priority and e not in ['(', ')']:
        print(e, end='')
    else:
        if not op_stack:
            op_stack.append(e)
        else:
            if e == ')':
                while op_stack[-1] != '(':
                    print(op_stack.pop(), end='')
                op_stack.pop()

            else:
                while op_stack and e != '(' and op_stack[-1] != '(' and \
                        priority[op_stack[-1]] >= priority[e]:
                    print(op_stack.pop(), end='')
                else:
                    op_stack.append(e)
while op_stack:
    print(op_stack.pop(), end='')
