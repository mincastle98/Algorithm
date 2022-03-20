# 만족도 설문 조사
# 만족ㅗ 설ㄴㅗㅏ 하

def main():
    n, m, k = list(map(int, input().split()))
    answers = [0 for _ in range(n+1)]
    friends = [[] for _ in range(n+1)]
    for _ in range(m):
        tmp = list(map(int, input().split()))
        answers[tmp[0]] = tmp[1]
    for _ in range(k):
        tmp = list(map(int, input().split()))
        friends[tmp[0]] += [tmp[1]]
        friends[tmp[1]] += [tmp[0]]

    graph = []
    visited = [0] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            tmp_group = [i]
            visited[i] = 1
            stack = friends[i][:]
            while stack:
                friend = stack.pop()
                if not visited[friend]:
                    tmp_group.append(friend)
                    visited[friend] = 1
                    stack += friends[friend]
            graph.append(tmp_group)

    total = 0
    n_ = 0
    for group in graph:
        mean = 0
        to_add = 0
        for i in group:
            if answers[i] != 0:
                mean += answers[i]
            else:
                to_add += 1

        if mean != 0:
            n_ += len(group)

        total += mean
        if len(group) - to_add != 0:
            mean //= len(group) - to_add
            total += mean * to_add

    answer = str(int((total / n_) * 100))
    print(answer[:-2] + "." + answer[-2:])


if __name__ == "__main__":
    main()
