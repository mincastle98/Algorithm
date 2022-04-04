# 2748 - 피보나치 수 2(B1)
n = int(input())

dp = [0, 1]
for _ in range(n-1):
    dp.append(dp[-1]+dp[-2])

print(dp[-1])
