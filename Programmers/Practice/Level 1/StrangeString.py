def solution(s):
    answer = ''
    cnt = 0

    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0
            continue
        if cnt & 1 == 1:
           s = s[:i] + s[i].lower() + s[i + 1:]
        else: s = s[:i] + s[i].upper() + s[i + 1:]

        cnt += 1
           
    answer = s
    
    return answer