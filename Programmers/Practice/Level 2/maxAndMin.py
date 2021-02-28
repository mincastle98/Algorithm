def solution(s):
    numList = s.split()
    numList = list(map(int, numList))

    answer = str(min(numList)) + " " + str(max(numList))

    return answer


print(solution("-1 -2 -3 -4"))
