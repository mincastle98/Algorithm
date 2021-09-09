# 숫자 문자열과 영단어

def solution(s):
    num = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]
    answer = ""

    while s:
        if s[0].isdigit():
            answer += str(s[0])
            s = s[1:]
        else:
            for i in range(3, 6):
                if s[0:i] in num:
                    answer += str(num.index(s[0:i]))
                    s = s[i:]
                    break

    return int(answer)


print(solution("one4seveneight"))
