# 4번째 점
def solution(aList, bList, cList):
    answer = []
    for a, b, c in zip(aList, bList, cList):
        if a == b:
            answer.append(c)
        elif a == c:
            answer.append(b)
        else:
            answer.append(a)

    print(" ".join(answer))


inputs1 = list(map(str, input().split(" ")))
inputs2 = list(map(str, input().split(" ")))
inputs3 = list(map(str, input().split(" ")))
solution(inputs1, inputs2, inputs3)
