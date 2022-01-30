# 2800 - 괄호 제거
from itertools import combinations

expression = input()

complete_bracket = []
temp_bracket = []
for idx, e in enumerate(expression):
    if e == '(':
        temp_bracket.append([idx])
    elif temp_bracket and e == ')':
        bracket = temp_bracket.pop()
        bracket.append(idx)
        complete_bracket.append(bracket)

answers = set()
for l in range(1, len(complete_bracket)+1):
    bracket_comb = list(combinations(complete_bracket, l))
    for comb in bracket_comb:
        for_print = list(expression)
        for c in comb:
            for_print[c[0]] = ""
            for_print[c[1]] = ""
        answers.add("".join(for_print))

answers = list(answers)
answers.sort()
for answer in answers:
    print(answer)
