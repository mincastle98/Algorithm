from itertools import combinations


def solution(orders, course):
    answer = []
    menuSet = set()
    for order in orders:
        for menu in order:
            menuSet.add(menu)
    menuSet = list(menuSet)

    for c in reversed(course):
        temp = {}
        courseSet = list(combinations(menuSet, c))
        for sets in courseSet:
            cnt = 0
            sets = list(sets)
            for order in orders:
                if len(order) < c:
                    continue
                order = list(order)
                check = all(elem in order for elem in sets)
                if check:
                    cnt += 1
            if cnt > 1:
                temp["".join(sets)] = cnt

        temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)

        if temp:
            maxValue = temp[0][1]
            for i in temp:
                if i[1] == maxValue:
                    answer.append(i)

    answer_ = []
    for sets in answer:
        tmp = "".join(sorted(list(sets[0])))
        answer_.append(tmp)
    answer = sorted(answer_)

    return answer


solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
