arr = list(map(int, input().split()))

ans = [1, 1]
increase, decrease = 1, 1

tmp = arr[0]
for i in arr:
    if i == tmp+1 or i == tmp+2:
        increase += 1
    else:
        if increase > ans[0]:
            ans[0] = increase
            increase = 1

    if i == tmp-1 or i == tmp-2:
        decrease += 1
    else:
        if decrease > ans[1]:
            ans[1] = decrease
            decrease = 1

    tmp = i

print(ans[0], ans[1])
