# 콜라츠 추측
def solution(num):
    answer = 0
    while num != 1 and answer <= 500:
        if int(num) & 1:
            num = num * 3 + 1
        else:
            num //= 2
        answer += 1

    if answer > 500:
        return -1
    else:
        return answer
