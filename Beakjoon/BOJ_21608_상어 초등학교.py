# 21608 - 상어 초등학교(S1)
from inspect import FrameInfo


N = int(input())
preferences = [list(map(int, input().split())) for _ in range(N**2)]

seats = [[0]*N for _ in range(N)]
preferences_dict = dict()
axis = dict()
dir = ((0, -1), (-1, 0), (1, 0), (0, 1))


def check_axis(y, x):
    return x >= 0 and y >= 0 and x < N and y < N


def find_seat():
    for c_ in range(4, -1, -1):
        for r in range(N):
            for c in range(N):
                cnt = 0
                if seats[r][c] == 0:
                    for d in dir:
                        if check_axis(r+d[1], c+d[0]) and seats[r+d[1]][c+d[0]] == 0:
                            cnt += 1
                if cnt == c_:
                    return (r, c)


for i in range(len(preferences)):
    student, preference = preferences[i][0], preferences[i][1:]
    preferences_dict[student] = preference
    can_sit = []
    for j in range(i):
        if preferences[j][0] in preference:
            can_sit.append(preferences[j][0])
    if not can_sit:
        y, x = find_seat()
        seats[y][x] = student
        axis[student] = (y, x)
    else:
        cand_seat = []
        for s in can_sit:
            for d in dir:
                if check_axis(axis[s][0]+d[1], axis[s][1]+d[0]) and seats[axis[s][0]+d[1]][axis[s][1]+d[0]] == 0:
                    cand_seat.append((axis[s][0]+d[1], axis[s][1]+d[0]))
        cand_seat.sort(key=lambda x: x[1])
        cand_seat.sort(key=lambda x: x[0])
        fix_seat = (N, N)
        friends = 0
        blank = 0
        for s in cand_seat:
            tmp_friends = 0
            tmp_blank = 0
            flag = False
            for d_ in dir:
                if check_axis(s[0]+d_[1], s[1]+d_[0]):
                    if seats[s[0]+d_[1]][s[1]+d_[0]] in can_sit:
                        tmp_friends += 1
                    elif seats[s[0]+d_[1]][s[1]+d_[0]] == 0:
                        tmp_blank += 1
                else:
                    flag = True
            if tmp_friends == 0 and tmp_blank == 0 and fix_seat == (N, N):
                fix_seat = (s[0], s[1])
            elif tmp_friends > friends or (tmp_friends == friends and tmp_blank > blank):
                fix_seat = (s[0], s[1])
                friends = tmp_friends
                blank = tmp_blank

        seats[fix_seat[0]][fix_seat[1]] = student
        axis[student] = (fix_seat[0], fix_seat[1])

answer = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for d in dir:
            if check_axis(r+d[1], c+d[0]) and seats[r+d[1]][c+d[0]] in preferences_dict[seats[r][c]]:
                cnt += 1
        answer += 10**(cnt-1) if cnt > 0 else 0

print(answer)
