import sys
from collections import deque

# 32484KB	120ms

n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append(sys.stdin.readline().rstrip())


# print(matrix)


def visit_matrix(start_x, start_y, graph, visited, group):
    dq = deque()

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    dq.append([start_x, start_y])
    visited[start_x][start_y] = 1

    while dq:
        x, y = dq.popleft()

        for d_x, d_y in zip(dx, dy):
            move_x = x + d_x
            move_y = y + d_y
            if move_x < 0 or move_x >= n or move_y < 0 or move_y >= n:
                continue

            if visited[move_x][move_y] == 0 and graph[move_x][move_y] in group:
                dq.append([move_x, move_y])
                visited[move_x][move_y] = 1


v = [[0 for _ in range(n)] for _ in range(n)]
seperate_cnt = 0
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            visit_matrix(i, j, matrix, v, matrix[i][j])
            seperate_cnt += 1

v = [[0 for _ in range(n)] for _ in range(n)]
color_weakness_cnt = 0
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            visit_matrix(i, j, matrix, v, ['B'] if matrix[i][j] == 'B' else ['R', 'G'])
            color_weakness_cnt += 1

print(seperate_cnt, color_weakness_cnt)
