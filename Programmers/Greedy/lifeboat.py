# 구명보트
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    idx = 0
    while idx < len(people):
        if people[idx] + people[-1] <= limit:
            people.pop()
        answer += 1
        idx += 1

    return answer


print(solution([70, 50, 80, 50], 100))
