# 없는 숫자 더하기
def solution(numbers):
    answer = -1

    num_list = [i for i in range(10)]
    for number in numbers:
        num_list[number] = 0
    answer = sum(num_list)

    return answer
