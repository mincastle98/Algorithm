# 1918 - 후위 표기식
expression = input()

stack = expression.split()

while stack:
    now = stack.pop()
    if now == ')':
        op_stack = []
        now = stack.pop()
        while now != '(':
