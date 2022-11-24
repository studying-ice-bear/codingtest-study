import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
maze = []

for _ in range(C):
    maze.append(list(t for t in sys.stdin.readline().strip()))

# print(*maze, sep='\n')

queue = deque()
visited = [[False for i in range(R)] for _ in range(C)]
timestamp = [[0 for _ in range(R)] for _ in range(C)]

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            queue.append((i, j, 'J'))
        elif maze[i][j] == 'F':
            queue.append((i, j, 'F'))
        else:
            # if maze[i][j] == '#':
            visited[i][j] = True
            timestamp[i][j] = -1
print(queue)

# bfs
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while queue:
    x, y, action = queue.popleft()
    print(x, y, action)
    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maze[nx][ny] == '.':
            visited[nx][ny] = True

            if action == 'J' and maze[nx][ny] == '.':
                maze[nx][ny] = 'J'
                queue.append((nx, ny, 'J'))
            elif action == 'F' and maze[nx][ny] == '.':
                maze[nx][ny] = 'F'
                queue.append((nx, ny, 'F'))
            timestamp[nx][ny] = timestamp[x][y] + 1

            print(*maze, sep='\n')
            print(*timestamp, sep='\n')

res = max(max(timestamp))
if res == -1:
    print("IMPOSSIBLE")
else:
    print(res+1)

'''
4 4
####
#JF#
#..#
#..#
output:
3

3 3
###
#F.
##J
output:
IMPOSSIBLE
'''