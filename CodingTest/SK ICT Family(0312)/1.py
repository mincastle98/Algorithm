def solution(money, costs):
    answer = 0

    values = [1, 5, 10, 50, 100, 500]
    cost_per_value = list(map(lambda x, y: x/y, costs, values))
    cost_per_value = list(zip(values, costs, cost_per_value))
    cost_per_value.sort(key=lambda x: x[0], reverse=True)
    cost_per_value.sort(key=lambda x: x[2])

    for v, c, _ in cost_per_value:
        cnt = money // v
        money -= v * cnt
        answer += c * cnt

    return answer

# 이거는 비용 / 화폐 단위 -> 가장 작은거부터 만들어가기 시작


print(solution(4578, [1, 4, 99, 35, 50, 1000]))
