import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False]*N for _ in range(N)]

'''
def dfs(x, y, change, cnt):
    visited[x][y] = True
    change.append((x, y))

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < N and 0 <= yy < N:
            if L <= abs(graph[x][y] - graph[xx][yy]) <= R and not visited[xx][yy]:
                visited[xx][yy] = True
                dfs(xx, yy, change, cnt+1)
                visited[xx][yy] = False


opened = [[False] * N for _ in range(N)]

def bfs(start):
    que = deque([start])
    x, y = start[0], start[1]

    visited[x][y] = True

    change = deque([start])

    while que:
        nx, ny = que.popleft()

        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if 0 <= xx < N and 0 <= yy < N:
                if L <= abs(graph[x][y] - graph[xx][yy]) <= R:
                    que.append((xx, yy))
                    change.append((xx, yy))
                    visited[x][y] = True
                    for i in range(4):
                        xxx = xx + dx[i]
                        yyy = yy + dy[i]
                        if 0 <= xxx < N and 0 <= yyy < N:
                            if (xxx, yyy) not in change:
                                visited[xxx][yyy] = True
                                change.append((xxx, yyy))
    n = len(change)
    total = 0
    for i in range(n):
        cx, cy = change[i][0], change[i][1]
        total += graph[cx][cy]
        print(total)
    # print(change)
    while change:
        cx, cy = change.popleft()
        graph[cx][cy] = total//n
        # print(round(total/n))


# bfs((0, 0))

def getResult(graph, c):
    total = 0
    n = len(c)
    for i in range(n):
        x, y = c[i][0], c[i][1]
        total += graph[x][y]

    while c:
        x, y = c.popleft()
        graph[x][y] = total // n

bfs((0, 0))
'''
# change = deque()
# dfs(0, 0, change)
# getResult(graph, change)
# print(*graph, sep='\n')

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
'''