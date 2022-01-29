# 13164 - 행복 유치원
N, K = list(map(int, input().split()))
students = list(map(int, input().split()))

gaps = []
for i in range(len(students)-1):
    gaps.append(students[i+1]-students[i])

gaps.sort(reverse=True)

print(sum(gaps[K-1:]))
