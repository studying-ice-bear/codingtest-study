import sys

input = sys.stdin.readline

N = int(input().rstrip())
video = []
for _ in range(N):
    video.append( input().rstrip())
# print(N, video)


# 색종이 만들기와 비슷한거 같다!

def traversal(x, y, N):
    color = video[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != video[i][j]:
                sys.stdout.write("(")
                traversal(x, y, N // 2)
                traversal(x, y + (N // 2), N // 2)
                traversal(x + (N // 2), y, N // 2)
                traversal(x + (N // 2), y + (N // 2), N // 2)
                sys.stdout.write(")")
                return 0
    sys.stdout.write(color)


traversal(0, 0, N)

# 30840KB 	72ms

