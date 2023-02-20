import sys
from collections import deque
import copy

def bfs():
    queue = deque()
    tmp = copy.deepcopy(graph)
    # 리스트안의 리스트는 deepcopy를 활용해야 한다! 참고하면 좋을 링크: https://wikidocs.net/16038
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx, ny))
    global answer
    cnt = 0

    for i in range(N):
        cnt += tmp[i].count(0)

    answer = max(answer, cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

N, M = map(int, sys.stdin.readline().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0
makeWall(0)
print(answer)

'''
import sys
from collections import deque
from itertools import combinations
import copy

N, M = map(int, sys.stdin.readline().split())
place = []
virus = []
wall = []
blank = []

for i in range(N):
    place.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if place[i][j] == 2:
            virus.append((i, j))
        elif place[i][j] == 1:
            wall.append((i, j))
        else:
            blank.append((i, j))

def bfs(graph, two = virus):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append(two[0])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 2 or graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                count += 1

    return count

safe = []

for combination in combinations(blank, 3):
    copy = place.copy()
    for c in combination:
        x = c[0]
        y = c[1]
        copy[x][y] = 1
    cnt = bfs(copy)
    safe.append(cnt)

print(max(safe))
'''

'''
8*8


7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

((0,0), (2,3), (2,4))
'''