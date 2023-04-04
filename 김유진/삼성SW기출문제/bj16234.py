import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def bfs(start):
    que = deque([start])
    x, y = start[0], start[1]

    visited[x][y] = True

    union = deque()
    union.append(start)

    while que:
        nx, ny = que.popleft()

        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy]:
                if L <= abs(graph[nx][ny] - graph[xx][yy]) <= R:
                    que.append((xx, yy))
                    visited[xx][yy] = True
                    union.append((xx, yy))

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

    total = 0
    n = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                total += graph[i][j]
                n += 1

    day += 1

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                graph[i][j] = total // n

    # print(*graph, sep='\n')

print(day)

# change = deque()
# dfs(0, 0, change)
# getResult(graph, change)


# day = 0
# while True:
#     day += 1
#     change = deque()
#     dfs(0, 0, change)
#     getResult(graph, change)
#     print(*graph, sep='\n')
#
#     check = True
#
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j]:
#                 check = False
#
#     if check:
#         break
#
# print(day)


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