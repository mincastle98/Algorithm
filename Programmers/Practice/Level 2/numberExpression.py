# 숫자의 표현
def solution(n):
    answer = 0

    i = 1
    while True:
        startNum = n // i
        if startNum < 1:
            break

        if i & 1:
            rule = [(i - 1) // 2, (i - 1) // 2]
        else:
            rule = [(i - 2) // 2, (i - 2) // 2 + 1]

        numList = [startNum]
        for f in range(1, rule[0] + 1):
            numList = [startNum - f] + numList
        if numList[0] < 1:
            break

        for b in range(1, rule[1] + 1):
            numList.append(startNum + b)

        if n == sum(numList):
            answer += 1
        i += 1

    return answer


print(solution(15))
