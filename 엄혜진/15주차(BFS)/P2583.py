import sys
from collections import deque

# 32484KB	104ms
def print_rec():
    for t in range(n):
        print(matrix[t])
    print()


m, n, k = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):

    lx, ly, rx, ry = map(int, sys.stdin.readline().rstrip().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            matrix[i][j] = -1

    # print_rec()


def bfs(x, y):
    cnt = 1
    dq = deque()

    dq.append([x, y])
    matrix[x][y] = cnt

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while dq:
        cur_x, cur_y = dq.popleft()
        for k in range(len(dx)):
            new_x = cur_x + dx[k]
            new_y = cur_y + dy[k]
            if 0 <= new_x < n and 0 <= new_y < m and matrix[new_x][new_y] == 0:
                dq.append([new_x, new_y])
                cnt += 1
                matrix[new_x][new_y] = cnt
    return cnt


answer = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            answer.append(bfs(i, j))

# print_rec()

print(len(answer))
answer.sort()
print(' '.join(map(str, answer)))
