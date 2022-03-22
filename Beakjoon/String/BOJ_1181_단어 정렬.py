# 1181 - 단어 정렬(S5)
N = int(input())
strings = list(set([input() for _ in range(N)]))
strings.sort()
strings.sort(key=lambda x: len(x))

for s in strings:
    print(s)
