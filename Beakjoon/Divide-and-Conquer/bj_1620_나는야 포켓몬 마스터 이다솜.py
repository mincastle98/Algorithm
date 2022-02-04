# 1620 - 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())

pocketmons_dict = dict()
pocketmons_list = []
questions = []
for i in range(N):
    tmp = input()
    pocketmons_dict[tmp] = i+1
    pocketmons_list.append(tmp)

for i in range(M):
    questions.append(input())

for question in questions:
    if question.isdigit():
        print(pocketmons_list[int(question)-1])
    else:
        print(pocketmons_dict[question])
