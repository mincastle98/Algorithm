# 1935 - 후위 표기식2
N = int(input())
expression = input()
op = dict()
for i in range(N):
    op[chr(ord('A')+i)] = int(input())

stack = []
for e in expression:
    if e.isalpha():
        stack.append(op[e])
    else:
        op2 = stack.pop()
        op1 = stack.pop()

        if e == "+":
            result = op1+op2
        elif e == "-":
            result = op1-op2
        elif e == "*":
            result = op1*op2
        elif e == "/":
            result = op1/op2

        stack.append(result)

print("%.2f" % stack[0])
