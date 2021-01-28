def solution(a, b):
    gap = b - a
    cnt = 0

    move = 0
    while gap > 0:
        cnt += 1
        if move == 0:
            move += 1
        elif gap >= (move + 1) * (move + 2) // 2:
            move += 1
        elif gap >= move * (move + 1) // 2:
            move = move
        else:
            move -= 1

        if move == 0:
            move += 1
        gap -= move

    print(cnt)


n = int(input())
inputList = []
for i in range(n):
    inputList.append(list(map(int, input().split(" "))))

for i in range(n):
    solution(inputList[i][0], inputList[i][1])
