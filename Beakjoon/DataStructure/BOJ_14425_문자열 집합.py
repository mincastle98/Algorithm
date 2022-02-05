# 13325 - 문자열 집합
N, M = list(map(int, input().split()))

str_list = dict()
for _ in range(N):
    tmp = input()
    str_list[tmp] = True

check_list = []
for _ in range(M):
    check_list.append(input())

ans = 0
for c in check_list:
    if str_list.get(c, False):
        ans += 1

print(ans)
