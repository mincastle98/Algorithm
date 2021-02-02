# 직사각형에서 탈출
def solution(inputs):
    x, y, w, h = inputs
    print(min([x, y, w - x, h - y]))


inputs = list(map(int, input().split(" ")))
solution(inputs)
