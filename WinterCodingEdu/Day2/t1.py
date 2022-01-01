N = int(input())
store_part = list(map(int, input().split()))
M = int(input())
customer_part = list(map(int, input().split()))
customer_part = [[customer_part[i], i]for i in range(len(customer_part))]

# 풀이 1
for c in customer_part:
    if c in store_part:
        print("yes", end=" ")
    else:
        print("no", end=" ")


# 풀이 2
# store_part.sort()
# customer_part.sort()

# ans = []
# idx_s, idx_c = 0, 0
# while len(ans) < len(customer_part):
#     if store_part[idx_s] == customer_part[idx_c][0]:
#         ans.append(["yes", customer_part[idx_c][1]])
#         idx_c += 1
#     else:
#         if store_part[idx_s] < customer_part[idx_c][0]:
#             idx_s += 1
#         elif store_part[idx_s] > customer_part[idx_c][0]:
#             ans.append(["no", customer_part[idx_c][1]])
#             idx_c += 1

# ans.sort(key=lambda x: x[1])
# ans = list(map(lambda x: x[0], ans))

# for a in ans:
#     print(a, end=" ")
