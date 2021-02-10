# 순위 검색
import bisect
from itertools import product


def solution(info, query):
    answer = []
    infoList = {}
    info1 = ['-', 'j', 'p', 'c']
    info2 = ['-', 'b', 'f']
    info3 = ['-', 'j', 's']
    info4 = ['-', 'p', 'c']
    for i1 in info1:
        for i2 in info2:
            for i3 in info3:
                for i4 in info4:
                    key = i1 + i2 + i3 + i4
                    infoList[key] = []

    for i in info:
        tmp = i.split(" ")
        for j in range(len(tmp[:-1])):
            tmp[j] = [tmp[j][0], '-']

        li = list(product(*tmp[:-1]))
        for j in li:
            infoList["".join(j)].append(int(tmp[-1]))

    for il in infoList:
        infoList[il].sort()

    for q in query:
        q = q.replace(" and ", " ").split(" ")
        q[-1] = int(q[-1])
        sq = [i[0] for i in q[:-1]]
        key = "".join(sq)
        target = infoList[key]
        ans = bisect.bisect_left(target, q[-1])

        answer.append(len(target) - ans)

    print(answer)
    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 149"])
