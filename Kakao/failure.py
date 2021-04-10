# 실패율
def solution(N, stages):
    user = [0 for i in range(N + 1)]
    failure = {}

    for s in stages:
        user[s - 1] += 1

    for i in range(N - 1, -1, -1):
        failure[i + 1] = user[i] / (user[i] + user[i + 1]) if user[i] + user[i + 1] != 0 else 0
        user[i] += user[i + 1]

    answer = sorted(failure.items(), key=(lambda x: x[0]))
    answer = sorted(answer, key=(lambda x: x[1]), reverse=True)
    answer = list(map(lambda x: x[0], answer))

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
