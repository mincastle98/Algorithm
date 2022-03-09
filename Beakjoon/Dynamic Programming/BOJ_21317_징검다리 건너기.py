# 21317 - 징검다리 건너기(S1)
import sys

N = int(sys.stdin.readline())
jump_cost = []
for i in range(N-1):
    jump_cost.append(list(map(int, sys.stdin.readline().split())))
k = int(sys.stdin.readline())

max_cost_idx = 0
max_cost = 0
for i in range(2, N-1):

    tmp = max(max_cost, max(jump_cost[i][0]+jump_cost[i-1][0]+jump_cost[i-2][0],
              jump_cost[i-2][1]+jump_cost[i][0], jump_cost[i-2][0]+jump_cost[i-1][1]))
    if tmp != max_cost:
        max_cost = tmp
        max_cost_idx = i

dp = [0] * N
for i in range(1, max_cost_idx-1):
    if i == 1:
        dp[i] = jump_cost[i-1][0]
    elif i == 2:
        dp[i] = min(dp[i-1]+jump_cost[i-1][0], jump_cost[i-2][1])
    else:
        dp[i] = min(dp[i-1]+jump_cost[i-1][0], dp[i-2]+jump_cost[i-2][1])
dp[max_cost_idx+1] = dp[i]+k
for i in range(max_cost_idx+2, N):
    if i == max_cost_idx+2:
        dp[i] = jump_cost[i-1][0]
    elif i == max_cost_idx+3:
        dp[i] = min(dp[i-1]+jump_cost[i-1][0], jump_cost[i-2][1])
    else:
        dp[i] = min(dp[i-1]+jump_cost[i-1][0], dp[i-2]+jump_cost[i-2][1])


print(dp[-1])

[0, 0, 0, 0]
