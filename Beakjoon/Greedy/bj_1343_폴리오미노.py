# 1343 - 폴리오미노
board = input().split(".")

for i in range(len(board)):
    if len(board[i]) % 2:
        print(-1)
        exit(0)
    else:
        idx = 0
        while idx < len(board[i]):
            if idx + 4 <= len(board[i]):
                board[i] = board[i][0:idx]+"AAAA"+board[i][idx+4:]
                idx += 4
            else:
                board[i] = board[i][0:idx]+"BB"+board[i][idx+2:]
                idx += 2

print(".".join(board))
