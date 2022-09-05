# 2018 KAKAO BLIND RECRUITMENT - 뉴스 클러스터링(Level 2)
def make_fragment(str):
    fragment = []
    for i in range(len(str) - 1):
        target = str[i:i + 2]
        if target.isalpha():
            fragment.append(str[i:i + 2])

    return fragment


def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    fragment1, fragment2 = make_fragment(str1), make_fragment(str2)

    intersection = set(fragment1) & set(fragment2)
    union = set(fragment1) | set(fragment2)

    inter_point, union_point = 0, 0
    for i in intersection:
        inter_point += min(fragment1.count(i), fragment2.count(i))
    for u in union:
        union_point += max(fragment1.count(u), fragment2.count(u))

    if union_point == 0:
        return 65536
    else:
        return int(65536 * inter_point / union_point)


ex1 = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
ex2 = ["french", "shake hands", "AAAA12", "e=m*c^2"]
for i in range(len(ex1)):
    print(solution(ex1[i], ex2[i]))
