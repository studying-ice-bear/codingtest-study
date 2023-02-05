'''
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
'''
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

move = [[0, -1], [0, 1], [1, 0], [-1, 0]]
days = 0

while queue:
    x, y = queue.popleft()

    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            queue.append((nx, ny))

res = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)
