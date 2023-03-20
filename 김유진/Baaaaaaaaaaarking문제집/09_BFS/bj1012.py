import sys
from collections import deque

def bfs(graph, a, b):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

def dfs(board, visited, position):
    stack = [position]
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        cur_i, cur_j = stack[-1]
        visited[cur_i][cur_j] = True

        for dx, dy in dr:
            i, j = cur_i+dx, cur_j+dy
            if 0 <= i < N and 0 <= j < M and board[i][j] and not visited[i][j]:
                stack.append((i, j))
                break

        else:
            stack.pop()

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # 가로 길이, 세로 길이, 배추 위치 개수
    garden = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        garden[y][x] = 1

    for i in range(N):
        for j in range(M):
            if garden[i][j] and not visited[i][j]:
                cnt += 1
                dfs(garden, visited, (i, j))


            # if garden[i][j]:
            #     bfs(garden, i, j)
            #     cnt += 1

    print(cnt)
