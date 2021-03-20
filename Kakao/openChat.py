# 오픈채팅방
def solution(record):
    answer = []
    state = {}
    inout = []
    for i, r in enumerate(record):
        rToken = r.split()
        if rToken[0] == "Enter":
            state[rToken[1]] = [rToken[2], True]
            inout.append(rToken[1])
        elif rToken[0] == "Leave":
            inout.append(rToken[1])
        elif rToken[0] == "Change":
            state[rToken[1]][0] = rToken[2]

    for i in inout:
        str = state[i][0] + "님이 "
        if state[i][1]:
            str += "들어왔습니다."
            state[i][1] = False
        else:
            str += "나갔습니다."
            state[i][1] = True
        answer.append(str)

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
