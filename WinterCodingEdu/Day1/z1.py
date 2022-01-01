N = int(input())

house = []
for i in range(N):
    house.append(int(input()))

# 풀이 1
print(max(house)-min(house))

# 풀이 2
# house_min, house_max = house[0], house[0]
# for i in house:
#     if i < house_min:
#         house_min = i
#     if i > house_max:
#         house_max = i

# print(house_max-house_min)
