# 소인수분해
def solution(num):
    i = 2
    while num > 1:
        while num % i == 0:
            print(i)
            num /= i

        i += 1


solution(int(input()))
