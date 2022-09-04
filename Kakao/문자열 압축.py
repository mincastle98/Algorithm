# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축(Level 2)
def solution(s):
    answer = 0

    # 문자 자르는 단위
    for i in range(1, len(s) + 1):
        pre_substring = ""
        cnt = 1
        temp = ""
        idx = 0
        while True:
            # 잘랐을 때 나머지 처리
            if idx + i > len(s):
                temp += str(cnt) + pre_substring if cnt > 1 else pre_substring
                temp += s[idx:]
                break

            # 앞이랑 같을 때
            if s[idx:idx + i] == pre_substring:
                cnt += 1
            else:  # 앞이랑 다를 때
                temp += str(cnt) + pre_substring if cnt > 1 else pre_substring
                cnt = 1
            pre_substring = s[idx:idx + i]
            idx += i

        answer = min(answer, len(temp)) if answer != 0 else len(temp)

    return answer


print(solution("aabbaccc"))
