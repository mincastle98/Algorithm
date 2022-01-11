# 1874 - 스택 수열
n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

stack = []
for_push = 1
ans = []
for i in range(n):
    flag = True
    while flag:
        if not stack:
            stack.append(for_push)
            for_push += 1
            ans.append("+")
        else:
            if stack[-1] == seq[i]:
                stack.pop()
                flag = False
                ans.append("-")
            elif stack[-1] < seq[i]:
                stack.append(for_push)
                for_push += 1
                ans.append("+")
            else:
                print("NO")
                exit(0)

for a in ans:
    print(a)
