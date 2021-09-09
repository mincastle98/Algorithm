# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    correct = 0
    erased = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            correct += 1
    answer = [7-correct-erased, 7-correct]
    for i in range(len(answer)):
        if answer[i] == 7:
            answer[i] = 6

    return answer


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
