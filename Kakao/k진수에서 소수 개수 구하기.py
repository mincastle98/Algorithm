# 2022 KAKAO BLIND RECRUITMENT - k진수에서 소수 개수 구하기(Level 2)
import math


def convert10toN(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    num_list = convert10toN(n, k).split('0')
    for num in num_list:
        if num in ["", "1"]:
            continue

        if is_prime(int(num)):
            answer += 1

    return answer


testcases = [(437674, 3), (110011, 10)]
for tc in testcases:
    print(solution(tc[0], tc[1]))
