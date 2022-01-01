import random

n = int(input())

# 풀이 1
arr = [(i+1, random.random()) for i in range(n)]
arr.sort(key=lambda x: x[1])
arr = list(map(lambda x: x[0], arr))

print(arr)


# 풀이 2
# arr = [i+1 for i in range(n)]
# random.shuffle(arr)

# print(list)
