N, M = map(int, input().split())
tteoks = list(map(int, input().split()))

tteoks.sort(reverse=True)
cutter = tteoks[0]-M

while True:
    sum = 0
    flag = 0
    for t in tteoks:
        sum += t-cutter if t-cutter > 0 else 0
        if sum > M:
            flag = 1
            break

    if flag:
        cutter += 1
    else:
        if sum < M:
            cutter -= 1
        break

print(cutter)
