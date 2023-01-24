# 도화지의 넓이가 가장 넓은 것
# 세로 크기 n (1~500)
# 가로 크기 m (1~500)

# 핵심 아이디어:
# 그림에서 1인 점을 찾아 bfs 알고리즘 돌리기

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
picture = []

for i in range(n):
    picture.append(list(map(int, sys.stdin.readline().split())))

# print(picture)

# (x, y)
# 좌 (x, y-1)
# 우 (x, y+1)
# 위 (x+1, y)
# 아래 (x-1, y)
move = [[0, -1], [0, 1], [1, 0], [-1, 0]]
visited = []


def bfs(graph, x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0

    size = 1
    while queue:
        q = queue.popleft()
        currentX, currentY = q[0], q[1]

        for dx, dy in move:
            nx = currentX + dx
            ny = currentY + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                size += 1

    return size

pictureSize = []

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            temp = bfs(picture, i, j)
            pictureSize.append(temp)

print(len(pictureSize))

if len(pictureSize) == 0:
    print(0)
else:
    print(max(pictureSize))

'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''