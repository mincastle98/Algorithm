# 124 나라의 숫자
def solution(n):
    answer = ''

    while n:
        if n % 3 == 0:
            answer = '4' + answer
            n -= 1
        elif n % 3 == 1:
            answer = '1' + answer
        elif n % 3 == 2:
            answer = '2' + answer
        n //= 3

    return answer