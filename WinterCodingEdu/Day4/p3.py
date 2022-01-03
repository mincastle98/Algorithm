x, y = map(int, input().split())

arr = [[] for _ in range(y)]
for i in range(y):
    arr[i] = list(map(int, input().split()))

n = int(input())

FAIL = n**2 + 1

arr_ = [[0 for _ in range(x)] for _ in range(y)]
for dx in range(x):
    for dy in range(y):
        flag = False
        size_err = False
        for i in range(n):
            if dx+i == x:
                size_err = True
                arr_[dx][dy] = FAIL
                break

            for j in range(n):
                if dy+j == y:
                    size_err = True
                    break

                if arr[dx+i][dy+j] == 2:
                    flag = True
                    break
                elif arr[dx+i][dy+j] == 1:
                    arr_[dx][dy] += 1

            if flag or size_err:
                arr_[dx][dy] = FAIL
                break

arr__ = []
for i in range(y):
    arr__ += arr_[i]

ans = min(arr__)
if ans == FAIL:
    ans = -1
print(ans)
