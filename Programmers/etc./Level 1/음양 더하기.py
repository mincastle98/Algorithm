# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for pair in zip(absolutes, signs):
        answer += pair[0] if pair[1] else pair[0]*(-1)

    return answer
