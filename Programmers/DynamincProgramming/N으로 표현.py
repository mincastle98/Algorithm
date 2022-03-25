# N으로 표현(Level 3)
def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(1, 9):
        for k in range(1, (i//2)+1):
            for op1 in list(dp[k]):
                for op2 in list(dp[i-k]):
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op2-op1)
                    dp[i].add(op1*op2)
                    dp[i].add(op1//op2 if op2 != 0 else 0)
                    dp[i].add(op2//op1 if op1 != 0 else 0)

        dp[i].add(N*int("1"*i))

        if number in dp[i]:
            answer = i
            break

    return answer
