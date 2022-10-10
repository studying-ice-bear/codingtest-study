import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = []
for _ in range(N):
    maze.append(sys.stdin.readline().rstrip())
visited = [[0 for i in range(M)] for j in range(N)]
# print(N, M, maze, visited)


# def dfs(E, x, y, current):
#     for i in range(len(visited)):
#         print(visited[i])
#     print()
#
#     if x < 0 or x >= N or y < 0 or y >= M:
#         return 0
#
#     visited[x][y] = current
#
#     if x == N - 1 and y == M - 1:
#         return 0
#
#     if 0 <= x + 1 < N and E[x + 1][y] == '1' and visited[x + 1][y] == 0:
#         dfs(E, x + 1, y, current + 1)
#     if 0 <= y + 1 < M and E[x][y + 1] == '1' and visited[x][y + 1] == 0:
#         dfs(E, x, y + 1, current + 1)
#     if 0 <= x - 1 < N and E[x - 1][y] == '1' and visited[x - 1][y] == 0:
#         dfs(E, x - 1, y, current + 1)
#     if 0 <= y - 1 < M and E[x][y - 1] == '1' and visited[x][y - 1] == 0:
#         dfs(E, x - 1, y, current + 1)
#
#
# dfs(maze, 0, 0, 1)
# 아.. 이건 bfs다.. 잘못 생각함

def bfs(E, x, y, current):
    dq = deque()
    visited[x][y] = current
    dq.append((x, y, current))
    while len(dq):
        x, y, current = dq.popleft()

        if 0 <= x + 1 < N and E[x + 1][y] == '1' and visited[x + 1][y] == 0:
            visited[x + 1][y] = current + 1
            dq.append((x + 1, y, current + 1))
        if 0 <= y + 1 < M and E[x][y + 1] == '1' and visited[x][y + 1] == 0:
            visited[x][y + 1] = current + 1
            dq.append((x, y + 1, current + 1))
        if 0 <= x - 1 < N and E[x - 1][y] == '1' and visited[x - 1][y] == 0:
            visited[x - 1][y] = current + 1
            dq.append((x - 1, y, current + 1))
        if 0 <= y - 1 < M and E[x][y - 1] == '1' and visited[x][y - 1] == 0:
            visited[x][y - 1] = current + 1
            dq.append((x, y - 1, current + 1))

bfs(maze, 0, 0, 1)

# for i in range(len(visited)):
#     print(visited[i])

print(visited[N-1][M-1])

# 32508KB	100ms