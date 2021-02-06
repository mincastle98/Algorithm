# 메뉴 리뉴얼
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        tmp = {}
        for order in orders:
            comList = combinations(order, c)

            for com in comList:
                com = "".join(sorted(list(com)))
                if com not in tmp:
                    tmp[com] = 1
                else:
                    tmp[com] += 1
        if tmp:
            tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
            maxValue = tmp[0][1]
            for t in tmp:
                if t[1] == maxValue and not maxValue == 1:
                    answer.append(t[0])
                else:
                    break

    answer = sorted(answer)
    print(answer)
    return answer


solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
