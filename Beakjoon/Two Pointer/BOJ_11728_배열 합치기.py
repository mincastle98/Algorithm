# 11728 - 배열 합치기(S5)
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

new_list = []

idx_a, idx_b = 0, 0
while idx_a < N or idx_b < M:
    if idx_a == N and idx_b < M:
        new_list.append(B[idx_b])
        idx_b += 1
    elif idx_a < N and idx_b == M:
        new_list.append(A[idx_a])
        idx_a += 1
    elif A[idx_a] <= B[idx_b]:
        new_list.append(A[idx_a])
        idx_a += 1
    else:
        new_list.append(B[idx_b])
        idx_b += 1

print(*new_list)
