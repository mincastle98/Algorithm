# 1138 - 한 줄로 서기(S2)
N = int(input())
info = list(map(int, input().split()))

sequence = [0]*N

for i in range(N):
    zero_list = list(filter(lambda x: sequence[x] == 0, range(N)))
    sequence[zero_list[info[i]]] = i+1

print(*sequence)
