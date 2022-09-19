import sys

input = sys.stdin.readline

N = int(input().rstrip())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().rstrip().split())))
# print(N, paper)
blue = 0
white = 0


def traversal(x, y, N):
    global blue, white

    color = paper[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != paper[row][col]:  # 이전 종이 색과 다르면
                traversal(x, y, N // 2)  # 기존 색종이를 4등분했을 때, 2사분면
                traversal(x, y + N // 2, N // 2)  # 기존 색종이를 4등분했을 때, 1사분면
                traversal(x + N // 2, y, N // 2)  # 기존 색종이를 4등분했을 때, 3사분면
                traversal(x + N // 2, y + N // 2, N // 2)  # 기존 색종이를 4등분했을 때, 4사분면
                return 0  # 현재 N 크기의 종이는 인정되지 않는다

    # 크기가 N * N 인 종이의 색이 모두 동일하다면 인정된다.
    if color == 0:
        white += 1
    else:
        blue += 1


traversal(0, 0, N)
print(white)
print(blue)

# 도저히 못 풀겠어서 검색해서 코드를 봐버렸다. 대신 코드에 대한 설명을 작성해봤다.
