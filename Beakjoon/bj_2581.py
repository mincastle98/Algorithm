from math import sqrt


def solution(m, n):
    prime = []

    for i in range(m, n + 1):
        flag = 1
        if i == 1: continue
        for j in range(2, int(sqrt(i)) + 1):
            if not i % j:
                flag = 0
                break

        if flag:
            prime.append(i)

    if prime:
        print(sum(prime))
        print(prime[0])
    else:
        print(-1)


input1 = int(input())
input2 = int(input())
solution(input1, input2)
