# 2020 KAKAO BLIND RECRUITMENT - 괄호 변환(Level 2)
def is_correct(p):
    stack = []
    for i in range(len(p)):
        if p[i] == "(":
            stack.append("(")
        elif p[i] == ")":
            if not stack:
                return False
            stack.pop()

    return False if stack else True


def is_balanced(p):
    return p.count("(") == p.count(")")


def get_correct(p):
    answer = ""
    idx = 2
    if not p:
        return ""

    while not is_balanced(p[:idx]):
        idx += 1

    u = p[:idx]
    v = p[idx:]

    if is_correct(u):
        answer += u + get_correct(v)
    else:
        answer += "(" + get_correct(v) + ")"
        for ui in u[1:-1]:
            answer += ")" if ui == "(" else "("

    return answer


def solution(p):
    answer = get_correct(p)

    return answer


ex = ["(()())()", ")(", "()))((()"]
for e in ex:
    print(solution(e))
