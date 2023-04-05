import math
import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def bfs(start):
    que = deque()
    que.append(start)

    x, y = start[0], start[1]
    visited[x][y] = True

    union = deque()
    union.append(start)

    # 연합 국가의 총 인구 수
    total = graph[x][y]

    while que:
        nx, ny = que.popleft()

        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if xx < 0 or xx >= N or yy < 0 or yy >= N:
                continue

            if visited[xx][yy]:
                continue

            if L <= abs(graph[nx][ny] - graph[xx][yy]) <= R:
                que.append((xx, yy))
                visited[xx][yy] = True
                union.append((xx, yy))
                total += graph[xx][yy]

    for x, y in union:
        graph[x][y] = math.floor(total / len(union))

    return len(union)

day = 0

while True:
    visited = [[False] * N for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    move = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs((i, j)) > 1:
                    move = True

    if not move:
        break

    day += 1

    # total = 0
    # n = 0
    # for i in range(N):
    #     for j in range(N):
    #         if visited[i][j]:
    #             total += graph[i][j]
    #             n += 1
    #
    # for i in range(N):
    #     for j in range(N):
    #         if visited[i][j]:
    #             graph[i][j] = total // n

    # print(*graph, sep='\n')

print(day)



'''
5 20 50
50 30 0 10 30
20 40 20 0 0
0 10 10 10 30
30 40 50 20 10
0 20 10 10 10

3 20 50
35 35 15
35 35 0
5 30 0

'''