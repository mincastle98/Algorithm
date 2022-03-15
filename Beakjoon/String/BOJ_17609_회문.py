# 17609 - 회문(S1)
import sys

T = int(sys.stdin.readline().strip())
strings = []
for _ in range(T):
    strings.append(sys.stdin.readline().strip())

for string in strings:
    axis = len(string)//2
    if string[:axis] == string[::-1][:axis]:
        print(0)
    else:
        for i in range(axis):
            if string[i] != string[-(i+1)]:
                if i:
                    tmp1 = string[i+1:-i]
                else:
                    tmp1 = string[1:]
                tmp2 = string[i:-(i+1)]
                if tmp1[:axis] == tmp1[::-1][:axis] or tmp2[:axis] == tmp2[::-1][:axis]:
                    print(1)
                else:
                    print(2)
                break
