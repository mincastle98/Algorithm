# 뉴스 클러스터링
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    tok1 = [str1[i:i + 2] for i in range(len(str1) - 1)]
    tok2 = [str2[i:i + 2] for i in range(len(str2) - 1)]

    tmp = set(tok1 + tok2)
    union, insec = [], []
    for t in tmp:
        if t[0].isalpha() and t[1].isalpha():
            union += [t] * max(tok1.count(t), tok2.count(t))
            insec += [t] * min(tok1.count(t), tok2.count(t))

    if len(union):
        return int((len(insec) / len(union)) * 65536)
    else:
        return 65536


print(solution("FRANCE", "french"))
