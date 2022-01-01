N = int(input())
fears = list(map(int, input().split()))
fears.sort(reverse=True)

ans = 0
tmp = []
for f in fears:
    tmp.append(f)
    if len(tmp) == tmp[0]:
        ans += 1
        tmp = []

print(ans)
