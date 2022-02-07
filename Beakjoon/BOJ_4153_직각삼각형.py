# 직각삼각형
def solution(inputs):
    for i in inputs:
        if i == [0, 0, 0]:
            break
        i.sort()
        if i[2] ** 2 == i[0] ** 2 + i[1] ** 2:
            print("right")
        else:
            print("wrong")


inputs = [list(map(int, input().split(" ")))]
while inputs[-1] != [0, 0, 0]:
    inputs.append(list(map(int, input().split(" "))))

solution(inputs)
