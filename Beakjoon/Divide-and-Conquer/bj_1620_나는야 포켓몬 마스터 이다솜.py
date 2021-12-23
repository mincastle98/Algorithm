# 1620 - 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())

pocketmons_dict = dict()
pocketmons_list = []
questions = []
for i in range(N):
    tmp = input()
    if pocketmons_dict[tmp[0]]:
        pocketmons_dict[tmp[0].lower()].append((i, tmp))
    else:
        pocketmons_dict[tmp[0].lower()] = (i, tmp)
    pocketmons_list.append(tmp)
for i in range(M):
    questions.append(input())


def solution():
    answers = []
    for question in questions:
        if question.isdigit():
            answers.append(pocketmons_list[int(question)-1])
        else:

            answers.append(pocketmons_dict[question[0].lower()
                                           ][pocketmons_dict[question[0].lower()].index(question)][0]+1)

    for answer in answers:
        print(answer)


solution()
