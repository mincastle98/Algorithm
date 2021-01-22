def solution(n):
    answer = 0
    reversedN = []

    while n > 0:
        reversedN.pend(n % 3)
        n = int(n / 3)
    print(reversedN)
    reversedN = list(reversed(reversedN))
    for i in range(len(reversedN)):
        answer += reversedN[i] * pow(3, int(i))

    return answer


solution(45)
