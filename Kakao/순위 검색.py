from bisect import bisect_left


def solution(info, query):
    answer = []

    info_list = [(i.split()[:-1], int(i.split()[-1])) for i in info]
    query_list = [("".join((q.replace(" and ", " ").split(" ")[:-1])), int(q.split()[-1])) for q in query]

    info_set = dict()
    info1 = ["cpp", "java", "python", "-"]
    info2 = ["backend", "frontend", "-"]
    info3 = ["junior", "senior", "-"]
    info4 = ["chicken", "pizza", "-"]
    # 조건 조합 딕셔너리 생성
    for i1 in info1:
        for i2 in info2:
            for i3 in info3:
                for i4 in info4:
                    key = i1 + i2 + i3 + i4
                    info_set[key] = []

    # 딕셔너리에 데이터 추가
    for i in info_list:
        for i1 in (i[0][0], "-"):
            for i2 in (i[0][1], "-"):
                for i3 in (i[0][2], "-"):
                    for i4 in (i[0][3], "-"):
                        key = i1 + i2 + i3 + i4
                        info_set[key].append(i[1])


    for keys in info_set.keys():
        info_set[keys].sort()

    for q in query_list:
        m = bisect_left(info_set[q[0]], q[1])
        answer.append(len(info_set[q[0]]) - m)

    return answer


ex1 = ["java backend junior pizza 150",
       "python frontend senior chicken 210",
       "python frontend senior chicken 150",
       "cpp backend senior pizza 260",
       "java backend junior chicken 80",
       "python backend senior chicken 50"]

ex2 = ["java and backend and junior and pizza 100",
       "python and frontend and senior and chicken 200",
       "cpp and - and senior and pizza 250",
       "- and backend and senior and - 150",
       "- and - and - and chicken 100",
       "- and - and - and - 150"]

print(solution(ex1, ex2))
