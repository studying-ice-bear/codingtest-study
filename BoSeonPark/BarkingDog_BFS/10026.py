import sys
from collections import deque
input = sys.stdin.readline


def bfs(b, v, c, i, j, n):    
    queue = deque([[i, j]])
    v[i][j] = True
    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while queue:
        x, y = queue.popleft()
        # v[x][y] = True
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n:
                if b[nx][ny] == c and v[nx][ny] == False:
                    queue.append([nx, ny])
                    v[nx][ny] = True
    
    
n = int(input())
board = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

ans1 = 0
ans2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(board, visited, board[i][j], i, j, n)
            ans1 += 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(board, visited, board[i][j], i, j, n)
            ans2 += 1

print(ans1, ans2)