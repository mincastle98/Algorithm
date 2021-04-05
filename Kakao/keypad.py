# 키패드 누르기
def getDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(numbers, hand):
    answer = ''
    now = [[0, 3], [2, 3]]  # col, row
    for n in numbers:
        if n == 0:
            target = [1, 3]
        else:
            target = [(n - 1) % 3, (n - 1) // 3]

        if n % 3 == 2 or n == 0:  # 2,5,8,0
            dis = [getDist(now[0], target), getDist(now[1], target)]
            if dis[0] < dis[1]:
                now[0] = target
                answer += "L"
            elif dis[0] > dis[1]:
                now[1] = target
                answer += "R"
            else:  # dis[0] == dis[1]
                if hand == "right":
                    now[1] = target
                    answer += "R"
                else:  # hand == "left"
                    now[0] = target
                    answer += "L"
        elif n % 3 == 1:  # 1,4,7
            now[0] = target
            answer += "L"
        elif n % 3 == 0:  # 3,6,9
            now[1] = target
            answer += "R"

    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
