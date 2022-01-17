# 14916 - 거스름돈
n = int(input())

changes = [[0, 0], [3, -1], [1, 0], [4, -1], [2, 0],
           [0, 1], [3, 0], [1, 1], [4, 0], [2, 1]]

ans = changes[n % 10]
ans[1] += (n // 10) * 2

if ans[0] < 0 or ans[1] < 0:
    print(-1)
else:
    print(ans[0]+ans[1])
