# 10798 - 세로읽기(B1)
strings = []
for _ in range(5):
    strings.append(input())

idx = 0
while strings:
    print(strings[idx][0], end="")
    strings[idx] = strings[idx][1:]
    if strings[idx] == "":
        strings.pop(idx)
    else:
        idx += 1
    if idx == len(strings):
        idx = 0
