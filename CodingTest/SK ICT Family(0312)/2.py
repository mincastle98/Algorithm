def move_point(now, next, i, cnt):
    if cnt % 2 == 0:
        if i % 2 == 0:
            now[1] += next[(cnt+i) % 4]
        else:
            now[0] += next[(cnt+i) % 4]
    else:
        if i % 2 == 0:
            now[0] += next[(cnt+i) % 4]
        else:
            now[1] += next[(cnt+i) % 4]

    return now


def solution(n, clockwise):
    startpoint = [[0, 0], [0, n-1], [n-1, n-1], [n-1, 0]]
    next = [1, 1, -1, -1]
    arr = [[0]*n for _ in range(n)]

    for i in range(4):
        now = startpoint[i]
        length = n-1
        cnt = 0
        value = 1

        while length > 0:
            for l in range(length):
                arr[now[0]][now[1]] = value
                value += 1

                if l == length-1:
                    now = move_point(now, next, i, cnt+1)
                    break
                else:
                    now = move_point(now, next, i, cnt)

            cnt += 1
            length -= 2
    if n % 2 == 1:
        arr[now[0]][now[1]] = value

    if clockwise:
        return arr
    else:
        for a in arr:
            a.reverse()
        return arr


print(solution(5, True))
