# 괄호 변환
def checkCorrect(p):
    if not p: return ""

    answer = ''
    u, v = "", p
    lcount, rcount = 0, 0
    s = []
    # u,v parsing
    for idx, b in enumerate(v):
        if lcount and lcount == rcount:
            u, v = v[:idx], v[idx:]
            break
        if b == "(":
            lcount += 1
        else:
            rcount += 1
    if not u: u, v = v, u

    # u correct bracket checking
    flag = True
    for b in u:
        if b == "(":
            s.append(b)
        else:
            if not s or s.pop() == ")":
                flag = False
                break

    # correct bracket
    if flag:
        answer += u
        answer += checkCorrect(v)
    else:  # incorrect bracket process
        answer += "("
        answer += checkCorrect(v)
        answer += ")"
        u = u[1:-1]
        for b in u:
            if b == "(":
                answer += ")"
            else:
                answer += "("
    print(answer)
    return answer


def solution(p):
    return checkCorrect(p)


print(solution("()))((()"))
