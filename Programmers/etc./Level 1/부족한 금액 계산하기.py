# 부족한 금액 계산하기
def solution(price, money, count):
    answer = -1
    cnt = 0
    for i in range(1, count+1):
        cnt += i

    answer = money - cnt * price
    if answer > 0:
        answer = 0
    return -answer
