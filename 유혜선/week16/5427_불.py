import sys
from collections import deque as dq
input = sys.stdin.readline
inf = int(10e9)

def bfs(i, j):  
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = dq([(i, j, 1)])

    while q:
        cur_i, cur_j, cur_seq = q.popleft()

        for di, dj in d:
            next_i, next_j = cur_i + di, cur_j + dj
            if not(0 <= next_i < h and 0 <= next_j < w):
                continue
            
            if building[next_i][next_j] == "." and cur_seq < fired[next_i][next_j]:
                fired[next_i][next_j] = cur_seq
                q.append((next_i, next_j, cur_seq + 1))



t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    
    building = []
    for i in range(h):
        building.append(list(input().rstrip()))

    fired = [[inf for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if building[i][j] == "*":
                fired[i][j] = 0
                bfs(i, j)
            if building[i][j] == "@":
                start = (i, j)
    print(fired)
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    q = dq([(start[0], start[1], 1)])
    answer = inf
    while q:
        cur_i, cur_j, cur_seq = q.popleft()
        for di, dj in d:
            next_i, next_j = cur_i + di, cur_j + dj

            if not(0 <= next_i < h and 0 <= next_j < w):
                answer = min(answer, cur_seq)
                continue
            if building[next_i][next_j] in "#\*":
                continue
            if fired[next_i][next_j] > cur_seq and not visited[next_i][next_j]:
                q.append((next_i, next_j, cur_seq + 1))
                visited[next_i][next_j] = True 
    
    print(answer if answer != inf else "IMPOSSIBLE")
