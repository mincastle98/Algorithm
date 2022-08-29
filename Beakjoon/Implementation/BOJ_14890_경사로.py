# 14890 - 경사로(G3)
def checkDup(list1, list2):
    return len(set(list1 + list2)) == len(list1 + list2)


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

roads = board + [list(map(lambda x: x[n], board)) for n in range(N)]

answer = 0
for road in roads:
    continuous_cnt = 1
    isPassable = True
    slope = []
    for i in range(1, N):
        if road[i] == road[i - 1]:  # 길의 높이가 같은 경우
            continuous_cnt = continuous_cnt + 1
        else:
            if road[i] == road[i - 1] + 1:  # 앞칸이 1칸 높을 때
                if continuous_cnt < L or not checkDup(list(range(i - L, i)), slope):
                    isPassable = False
                    break
                slope += range(i - L, i)
                continuous_cnt = 1
            elif road[i] == road[i - 1] - 1:  # 앞칸이 1칸 낮을 때
                if road[i:i + L].count(road[i - 1] - 1) != L \
                        or not checkDup(list(range(i, i + L)), slope):
                    isPassable = False
                    break
                slope += range(i, i + L)
                continuous_cnt = 1
            else:  # 앞칸과의 높이 차가 1이 아닐 때
                isPassable = False
                break
    if isPassable:
        answer += 1

print(answer)
