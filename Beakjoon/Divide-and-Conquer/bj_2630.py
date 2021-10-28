# 색종이 만들기
cnt = [0, 0]     # white, blue

def checkPiece(paper, x, y, size):
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    
    for d in range(4):
        startX, startY = x + dx[d]*size, y + dy[d]*size
        color = paper[startX][startY]

        flag = 0
        for i in range(size):
            for j in range(size):
                if color != paper[startX + i][startY + j]:
                    flag = 1
                    break
            if flag: break
        
        if not flag:
            cnt[color] += 1
        else: 
            checkPiece(paper, x, y, size // 2)


def solution(N, paper):
    checkPiece(paper, 0, 0, N // 2)

    print(cnt)
    return  0


N = int(input())
paper = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    paper[i] = list(map(int, input().split()))
solution(N, paper)