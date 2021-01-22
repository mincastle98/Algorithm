# def solution(number, k):
#     answer = []
#     numList = [i for i in number]
#     length = len(numList) - k
#
#     for cnt in range(len(numList)-k):
#         maxNum = max(numList[:len(numList) - length + 1 + len(answer)])
#         answer.append(maxNum)
#         numList = numList[numList.index(maxNum)+1:]
#
#     answer = "".join(answer)
#     return answer

def solution(number, k):
    answer = []
    numList = [i for i in number]

    maxIdx = 0
    for cnt in range(len(numList)-k-1, -1, -1):
        if cnt == 0:
            toComp = numList[maxIdx:]
        else:
            toComp = numList[maxIdx:-cnt]

        maxNum = '0'
        maxIdx_ = 0
        for i in range(len(toComp)):
            if toComp[i] > maxNum:
                maxNum = toComp[i]
                maxIdx_ = i + 1
            if maxNum == '9':
                break

        maxIdx += maxIdx_
        answer.append(maxNum)

    answer = "".join(answer)
    return answer
