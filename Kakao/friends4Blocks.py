# 프렌즈4블록
def solution(m, n, board):
    answer = 0
    board = [[element for element in t] for t in zip(*board)]
    for i in range(len(board[0])):
        board[i] = list(reversed(board[i]))

    flag = True
    while flag:
        pop = []
        for col in range(len(board) - 1):
            for row in range(len(board[col]) - 1):
                if row + 1 < len(board[col + 1]) and board[col][row] == board[col + 1][row] \
                        == board[col][row + 1] == board[col + 1][row + 1]:
                    pop += [[col, row], [col + 1, row], [col, row + 1], [col + 1, row + 1]]
        if pop:
            pop.sort()
            cnt = 0
            for p in range(len(pop)):
                if pop.count(pop[p - cnt]) > 1:
                    pop.pop(pop.index(pop[p - cnt]))
                    cnt += 1

            for p in pop:
                board[p[0]][p[1]] = " "

            for b in board:
                while " " in b:
                    b.remove(" ")

            answer += len(pop)
        else:
            flag = False

    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
