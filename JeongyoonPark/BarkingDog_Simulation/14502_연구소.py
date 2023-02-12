import copy
from sys import stdin
from collections import deque
from itertools import combinations
input = stdin.readline

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
n, m = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(n)] 

wall = []
virus = deque()
for i in range(n):
        for j in range(m):
            if laboratory[i][j] == 2:
                virus.append((i,j))
            elif laboratory[i][j] == 0:
                wall.append((i,j))


def bfs(graph):
    cur_virus = copy.deepcopy(virus)
    while cur_virus:
        x, y = cur_virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                cur_virus.append((nx,ny))
    return graph

def count_zero(graph):
    answer = 0
    for g in graph:
        answer += g.count(0)
    return answer

max_result = 0
for combi in combinations(wall, 3):
    graph = copy.deepcopy(laboratory)
    for c in combi: graph[c[0]][c[1]] = 1
    answer = count_zero(bfs(graph))

    if answer > max_result: max_result = answer

print(max_result)



'''
아이디어 생각
1. 벽을 세울 수 있는 빈 공간을 입력 받을 때 넣어둠.
2. 그 중 3개씩 벽을 세울 수 있으니 브루트포스
3. 첫번 째 벽을 세웠을 때 bfs 결과 확인
'''