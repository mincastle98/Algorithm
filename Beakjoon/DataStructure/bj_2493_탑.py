# 2493 - 탑
N = int(input())
towers = list(map(int, input().split()))

answers = dict()
stack = []
for i in range(len(towers)-1, -1, -1):
    while stack and stack[-1][0] < towers[i]:
        answers[stack[-1][1]] = i+1
        stack.pop()

    if not stack or stack[-1][0] > towers[i]:
        stack.append((towers[i], i))

for s in stack:
    answers[s[1]] = 0

for i in range(N):
    print(answers[i], end=" ")
