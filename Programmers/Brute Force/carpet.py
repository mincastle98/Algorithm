def solution(brown, yellow):
    answer = []

    w = 3
    while True:
        if yellow - ((w - 2) * (brown / 2 - w)) == 0:
            answer.append(w)
            answer.append(int(brown / 2 - w + 2))

            answer = sorted(answer, reverse=True)
            return answer
        else: w += 1