def solution():
    answer = 0
    n = input()
    strList = []
    for i in range(int(n)):
        strList.append(input())

    for i in strList:
        tmp = []
        for j in range(len(i)):
            tmp.append((i[j], j))
        tmp = sorted(tmp)

        flag = 1
        for j in range(len(tmp)-1):
            if tmp[j][0] == tmp[j + 1][0] and tmp[j][1] + 1 != tmp[j + 1][1]:
                flag = 0
                break

        if flag:
            answer += 1

    print(answer)

solution()
