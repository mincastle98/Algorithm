k = int(input())
food_times = list(map(int, input().split()))
food_idx = [i for i in range(len(food_times))]

idx = 0
for i in range(k):
    food_times[food_idx[idx]] -= 1

    if food_times[food_idx[idx]] == 0:
        food_idx.pop(idx)
        idx -= 1

    if not food_idx:
        print(-1)
        break
    idx = (idx + 1) % len(food_idx)

print(food_idx[idx]+1)
