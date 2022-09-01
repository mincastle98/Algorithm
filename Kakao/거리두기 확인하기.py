# 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기(Level 2)
def check_axis(y, x):
    return 0 <= y < 5 and 0 <= x < 5


def solution(places):
    answer = []
    dir = ((-1, 0), (0, -1), (1, 0), (0, 1))

    for i in range(5):
        isCorrect = True
        room = places[i]
        stack = []
        for y in range(5):
            for x in range(5):
                if room[y][x] == "P":
                    stack.append([[y, x], 0])

        while stack:
            now = stack.pop()
            if now[1] == 0:
                for dy, dx in dir:
                    if not check_axis(now[0][0] + dy, now[0][1] + dx):
                        continue
                    if room[now[0][0] + dy][now[0][1] + dx] == "P":
                        isCorrect = False
                        break
                    if room[now[0][0] + dy][now[0][1] + dx] == "O":
                        stack.append([[now[0][0] + dy, now[0][1] + dx], 1])
            elif now[1] == 1:
                cnt = 0
                for dy, dx in dir:
                    if not check_axis(now[0][0] + dy, now[0][1] + dx):
                        continue
                    if room[now[0][0] + dy][now[0][1] + dx] == "P":
                        cnt += 1
                if cnt != 1:
                    isCorrect = False
                    break

        answer.append(1 if isCorrect else 0)

    return answer
