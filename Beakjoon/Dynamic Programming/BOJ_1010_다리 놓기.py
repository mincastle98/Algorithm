# 1010 - 다리 놓기(S5)
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    N = min(N, M-N)

    factorial = [1, 1]
    for i in range(2, M+1):
        factorial.append(factorial[-1]*i)

    print(int(factorial[M]/(factorial[M-N]*factorial[N])))
