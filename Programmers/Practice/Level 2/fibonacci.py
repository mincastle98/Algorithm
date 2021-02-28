# 피보나치 수
def solution(n):
    prev1 = 0
    prev2 = 0
    for i in range(n + 1):
        if i == 0 or i == 1:
            now = i
        else:
            now = prev1 + prev2
        prev2 = prev1
        prev1 = now

    return now % 1234567


print(solution(5))
