'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

answer:
((110(0101))(0010)1(0001))
'''
import sys
N = int(sys.stdin.readline())
video = [sys.stdin.readline() for _ in range(N)]

def check(x, y, n):
    pixel = video[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if pixel != video[i][j]:
                check(x, y, N//2)
                check(x + N // 2, y, N // 2)
                check(x, y+N//2, N//2)
                check(x+ N // 2, y + N // 2, N // 2)
                return
