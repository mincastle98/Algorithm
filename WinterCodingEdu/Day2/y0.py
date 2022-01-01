s = list(input())

# 풀이 1
ans = 0

op1 = int(s.pop(0))
while s:
    op2 = int(s.pop(0))

    if op1 * op2 > op1 + op2:
        op1 *= op2
    else:
        op1 += op2

print(op1)


# 풀이 2
# ans = 0

# op1 = int(s[0])
# for i in range(1, len(s)):
#     op2 = int(s[i])

#     if op1 * op2 > op1 + op2:
#         op1 *= op2
#     else:
#         op1 += op2

# print(op1)
