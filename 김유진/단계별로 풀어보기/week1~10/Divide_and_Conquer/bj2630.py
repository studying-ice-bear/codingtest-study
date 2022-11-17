import sys
N = int(sys.stdin.readline())
papper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(papper)
blue = 0
white = 0

def check(x, y, N):
    global white, blue
    color = papper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != papper[i][j]:
                check(x, y, N//2)
                check(x, y+N//2, N//2)
                check(x+N//2, y, N//2)
                check(x + N // 2, y+N//2, N // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

check(0, 0, N)
print(white)
print(blue)