from collections import deque

N, L, R = map(int, input().split())
land = []

for _ in range(N):
    land.append(list(map(int, input().split())))


def bfs(x, y, graph, visited):
    que = deque()
    que.append((x, y))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = True

    change = deque()
    change.append((x, y))

    while que:
        xx, yy = que.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and L <= abs(graph[xx][yy] - graph[nx][ny]) <= R:
                visited[nx][ny] = True
                que.append((nx, ny))
                change.append((nx, ny))

    print(change)

    total = 0
    cn = len(change)
    for i in range(cn):
        cx, cy = change[i][0], change[i][1]
        total += graph[cx][cy]

    while change:
        cx, cy = change.popleft()
        graph[cx][cy] = round(total / cn)



day = 0
while True:
    vis = [[False] * N for _ in range(N)]
    bfs(0, 0, land, vis)

    check = True
    for i in range(N):
        for j in range(N):
            if vis[i][j]:
                check = False

    if check:
        break
    else:
        day += 1

print(day)

