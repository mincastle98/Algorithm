from itertools import combinations


def main():
    n, m, k = list(map(int, input().split()))
    customers = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        customers[i] = list(map(lambda x: int(x >= 5), customers[i]))
        tmp = []
        for j in range(m):
            if customers[i][j]:
                tmp.append(j)
        customers[i] = tmp

    combs = list(combinations(range(m), k))

    min_cnt = n
    for c in combs:
        cnt = 0
        for i in range(n):
            if not set(customers[i]) - set(c):
                cnt += 1
        min_cnt = min(min_cnt, cnt)

        if min_cnt == n:
            break

    print(n - min_cnt)


if __name__ == "__main__":
    main()
