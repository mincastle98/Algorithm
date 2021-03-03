# JadenCase 문자열 만들기
def solution(s):
    s = s.lower()
    s = list(s)

    flag = 1
    for i in range(len(s)):
        if s[i] == " ":
            flag = 1
            continue

        if flag and s[i].isalpha():
            s[i] = s[i].upper()
        flag = 0

    answer = "".join(s)
    return answer


print(solution("3people unFollowed me"))
