# 타겟 넘버
def solution(numbers, target):
    answer = 0
    s = [[0, 0]]

    while s:
        level, value = s.pop()

        if level < len(numbers):
            s.append([level + 1, value - numbers[level]])
            s.append([level + 1, value + numbers[level]])
        else:
            if value == target:
                answer += 1

    return answer
