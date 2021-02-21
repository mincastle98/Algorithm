# 다음 큰 숫자
def solution(n):
    cnt = 0

    n_ = n
    while n_ > 0:
        if n_ & 1:
            cnt += 1
        n_ >>= 1
    answer = n + 1

    while True:
        answer_ = answer
        cnt_ = 0
        while answer_ > 0:
            if answer_ & 1:
                cnt_ += 1
            answer_ >>= 1

        if cnt_ == cnt:
            break
        else:
            answer += 1

    return answer


print(solution(78))
