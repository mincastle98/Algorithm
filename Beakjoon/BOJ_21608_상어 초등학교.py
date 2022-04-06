# 21608 - 상어 초등학교(S1)
N = int(input())
preferences = [list(map(int, input().split())) for _ in range(N**2)]

seats = [[0]*N for _ in range(N)]


def find_seat():
    dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for c in range(4, -1, -1):
        for r in range(N):
            for c in range(N):
                if seats[c][r] != 0:
                    for d in dir:
                        if


for i in range(len(preferences)):
    student, preference = preferences[i][0], preferences[i][1:]
    can_sit = []
    for j in range(i):
        if preferences[j][0] in preference:
            can_sit.append(preferences[j][0])
    if not can_sit:
