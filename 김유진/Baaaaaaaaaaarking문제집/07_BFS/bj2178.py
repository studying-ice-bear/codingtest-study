'''
 미로에서 빠져나가기
 (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수
'''

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(int(i) for i in sys.stdin.readline().strip()))

visited = [[False for _ in range(M)] for _ in range(N)]
count = [[0 for _ in range(M)] for _ in range(N)]

# (x, y)
# 좌 (x, y-1)
# 우 (x, y+1)
# 위 (x+1, y)
# 아래 (x-1, y)
move = [[0, -1], [0, 1], [1, 0], [-1, 0]]

def bfs(x=0, y=0):
    queue = deque()
    queue.append((x, y))
    count[x][y] = 1

    while queue:
        xx, yy = queue.popleft()

        for dx, dy in move:
            nx = xx + dx
            ny = yy + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 1 and visited[nx][ny] is False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count[nx][ny] = count[xx][yy] + 1

bfs()
print(count[-1][-1])
'''
4 6
101111
101010
101011
111011
'''
