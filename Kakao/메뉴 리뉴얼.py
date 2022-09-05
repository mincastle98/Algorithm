# # 2021 KAKAO BLIND RECRUITMENT - 메뉴 리뉴얼(Level 2)
from itertools import combinations


def solution(orders, course):
    answer = []
    # 코스 메뉴 구성
    for c in course:
        order_cnt = []
        combi = []
        for order in orders:
            combi += list(combinations(sorted(order), c))
        combi_unique = list(set(combi))

        for comb in combi_unique:
            order_cnt.append(combi.count(comb))

        max_order_cnt = max(order_cnt) if order_cnt else 1
        if max_order_cnt != 1:
            while max(order_cnt) == max_order_cnt:
                answer.append(combi_unique[order_cnt.index(max_order_cnt)])
                order_cnt[order_cnt.index(max_order_cnt)] = 0

    answer = sorted(list(map(lambda x: "".join(x), answer)))

    return answer


ex = [[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]],
      [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]],
      [["XYZ", "XWY", "WXA"], [2, 3, 4]]]

for e in ex:
    print(solution(e[0], e[1]))
