# 22857 - 가장 긴 짝수 연속한 부분 수열(S2)
S, K = map(int, input().split())
s = list(map(int, input().split()))

end = 0
cnt = 0
size = 0
flag = 1
answer = 0
for start in range(S):
    while cnt <= K and flag:
        if s[end] % 2:
            if cnt == K:
                break
            cnt += 1
        size += 1
        if end == S - 1:
            flag = 0
            break
        end += 1

    answer = max(answer, size-cnt)

    if s[start] % 2:
        cnt -= 1
    size -= 1

print(answer)
