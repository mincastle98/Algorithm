# n진수 게임
def convertFormat(n, type):
    answer = []
    while n > 0:
        tmp = n % type
        if tmp >= 10:
            answer.append(chr(55 + tmp))
        else:
            answer.append(tmp)
        n //= type
    if answer:
        return reversed(answer)
    else:
        return [0]


def solution(n, t, m, p):
    answer = ''
    num = 0
    player = 0
    while len(answer) < t:
        tmp = convertFormat(num, n)
        for i in tmp:
            if player % m == p - 1:
                answer += str(i)
                if len(answer) == t: break
            player += 1
        num += 1
    return answer


print(solution(2, 4, 2, 1))
