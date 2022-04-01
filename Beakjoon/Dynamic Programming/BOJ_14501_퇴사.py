# 14501 - 퇴사(S3)
N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

for i in range(len(schedules)-1, -1, -1):
    if i + schedules[i][0] > N:
        schedules[i] = [0, 0]

dp = [0] * N
for i in range(N-1, -1, -1):
    if i+schedules[i][0] < N:
        dp[i] = schedules[i][1] + max(dp[i+schedules[i][0]:])
    elif i+schedules[i][0] == N:
        dp[i] = schedules[i][1]

print(max(dp))
