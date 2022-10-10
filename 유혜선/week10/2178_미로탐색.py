"""
- 그래프와 순회(BFS)

idea> 1인 곳만 확인하면서 이전 경로 + 1 해주기

"""
import sys
from collections import deque as dq

input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
maze = []
for _ in range(n):
    temp = list(map(int, list(input().rstrip())))
    maze.append(temp)

# print(maze)
q = dq([(0, 0)])

while q:
    r, c = q.popleft()

    for dr, dc in d:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1:
            maze[nr][nc] = maze[r][c] + 1
            q.append((nr, nc))

print(maze[n-1][m-1])
