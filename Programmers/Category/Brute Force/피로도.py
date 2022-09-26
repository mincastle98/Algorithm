# 피로도(Level 2)
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    courses = list(permutations(dungeons, len(dungeons)))
    for course in courses:
        stamina = k
        enter_cnt = 0
        for dungeon in course:
            if stamina >= dungeon[0]:
                enter_cnt += 1
                stamina -= dungeon[1]
            else:
                break
        answer = max(answer, enter_cnt)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
