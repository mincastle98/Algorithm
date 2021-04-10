# 방금그곡
def solution(m, musicinfos):
    answer = {}
    for music in musicinfos:
        mList = music.split(",")

        tmp = []
        for i in mList[3]:
            if i.isalpha():
                tmp.append(i)
            else:
                tmp[-1] += i
        mList[3] = tmp

        runningTime = int(mList[1][3:]) - int(mList[0][3:]) + (int(mList[1][:2]) - int(mList[0][:2])) * 60
        running = mList[3] * (runningTime // len(mList[3])) + mList[3][:runningTime % len(mList[3])]

        for i in range(len(running)):
            if "".join(running[i:i + len(m) - m.count("#")]) == m:
                answer[mList[2]] = runningTime

    answer = sorted(answer.items(), key=(lambda x: x[1]), reverse=True)

    if answer:
        return answer[0][0]
    else:
        return "(None)"


print(solution("ABC", ["13:50,14:00,HELLO!,CDEFGAB", "12:00,12:10,HELLO2,CDEFGAB", "12:00,12:14,HELLO,CDEFGAB",
                       "13:00,13:14,WORLD,ABCDEF"]))
