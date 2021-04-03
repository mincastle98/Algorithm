# 후보키
from itertools import combinations


def makeKey(key, relation):
    list = []
    for r in relation:
        tmp = ""
        for i in key:
            tmp += r[i] + " "
        list.append(tmp)

    return list


# 후보키
def solution(relation):
    answer = 0
    used = []
    for i in range(1, len(relation[0]) + 1):
        combList = list(combinations(range(len(relation[0])), i))
        for c in combList:
            candidates = makeKey(c, relation)
            candidates_ = list(set(candidates))
            if len(candidates) == len(candidates_):
                flag = True
                for u in used:
                    if u & set(c) == u:
                        flag = False
                        break
                if flag:
                    answer += 1
                    used.append(set(c))

    return answer


print(solution([["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]]))
