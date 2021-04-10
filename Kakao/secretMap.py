# 비밀지도
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += str(((arr1[i] | arr2[i]) >> j) & 1)
        tmp = tmp.replace("1", "#")
        tmp = tmp.replace("0", " ")
        tmp = tmp[::-1]
        answer.append(tmp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
