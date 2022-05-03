# 경주로 건설(Level 3)
def check_yx(yx, size):
    return 0 <= yx[0] < size and 0 <= yx[1] < size


def solution(board):
    answer = 0

    board_size = len(board)
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    cost_board = [[0] * board_size for _ in range(board_size)]

    stack = [{"yx": [0, 0], "cost": 0, "visited": [item[:] for item in board], "dir": -1}]
    stack[0]["visited"][0][0] = 1
    while stack:
        now = stack.pop()
        if now["yx"] == [board_size - 1, board_size - 1]:
            answer = (min(answer, now["cost"]) if answer != 0 else now["cost"])
        else:
            for i, d in enumerate(dirs):
                next = dict()
                next["yx"] = [now["yx"][0] + d[0], now["yx"][1] + d[1]]
                y, x = next["yx"]
                if check_yx(next["yx"], board_size) and now["visited"][y][x] == 0:
                    if now["dir"] == -1 or now["dir"] == i:
                        next["cost"] = now["cost"] + 100
                    else:
                        next["cost"] = now["cost"] + 600
                    next["visited"] = [item[:] for item in now["visited"]]
                    next["visited"][y][x] = 1
                    next["dir"] = i

                    if cost_board[y][x] == 0 \
                            or min(cost_board[y][x] + 500, next["cost"]) == next["cost"]:
                        cost_board[y][x] = next["cost"]
                        stack.append(next)

    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
