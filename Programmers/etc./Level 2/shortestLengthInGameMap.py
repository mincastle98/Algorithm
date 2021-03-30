# 게임 맵 최단거리
from copy import deepcopy
from queue import Queue


def solution(maps):
    answer = []
    dxdy = [[0, 1], [1, 0], [-1, 0], [0, -1]]  # R U L D
    queue = Queue()
    queue.put([[0, 0], 1, deepcopy(maps)])
    while not queue.empty():
        now = queue.get()
        nowMap = deepcopy(now[2])
        nowMap[now[0][0]][now[0][1]] = 0
        if now[0] == [len(maps) - 1, len(maps[0]) - 1]:
            answer.append(now[1])
        for d in dxdy:
            after = [now[0][0] + d[0], now[0][1] + d[1]]
            if after == [len(maps) - 1, len(maps[0]) - 1]:
                answer.append(now[1] + 1)
                break
            if 0 <= after[0] < len(maps) and 0 <= after[1] < len(maps[0]) and now[2][after[0]][after[1]]:
                queue.put([after, now[1] + 1, nowMap])

    if answer:
        return min(answer)
    else:
        return -1


print(solution([[1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1]]))
