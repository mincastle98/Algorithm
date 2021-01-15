def solution(s):
    cnt = 0
    changed = ""

    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0
            changed += ' '
            continue

        if cnt & 1:
           changed += s[i].lower()
        else: changed +=s[i].upper()

        cnt += 1
    
    return changed