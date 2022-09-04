# 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방(Level 2)
def solution(record):
    answer = []
    nicknames = dict()

    for r in record:
        log = r.split()
        if log[0] in ["Enter", "Change"]:
            nicknames[log[1]] = log[2]

    for r in record:
        log = r.split()
        if log[0] == "Enter":
            answer.append(nicknames[log[1]] + "님이 들어왔습니다.")
        elif log[0] == "Leave":
            answer.append(nicknames[log[1]] + "님이 나갔습니다.")

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
