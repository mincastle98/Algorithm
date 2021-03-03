# 땅따먹기
def solution(land):
    maxIdx = land[0].index(max(land[0]))
    first = land[0][maxIdx]
    land[0][maxIdx] = 0
    second = max(land[0])

    for c in land[1:]:
        for ri in range(4):
            if ri == maxIdx:
                c[ri] += second
            else:
                c[ri] += first

        maxIdx = c.index(max(c))
        first = c[maxIdx]
        c[maxIdx] = 0
        second = max(c)

    return first
