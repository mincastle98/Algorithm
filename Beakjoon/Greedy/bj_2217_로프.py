# 2217 - 로프
N = int(input())
ropes = []
for i in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)

cnt = 0
maxWeight = ropes[0]
for rope in ropes:
    cnt += 1
    maxWeight = max(maxWeight, rope * cnt)

print(maxWeight)
