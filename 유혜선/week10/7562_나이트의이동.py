"""
- 그래프와 순회(BFS)

idea> 시작점부터 나이트의 이동할 수 있는 경로를 체크
- 방문할때마다 전에 방문한 값에 1을 더해서 저장 (움직인 횟수)
- bfs 이용

"""
import sys
from collections import deque as dq
input = sys.stdin.readline

def BFS(r, c):
    d = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
        (1, -2), (2, -1), (2, 1), (1, 2)]
    
    q = dq([(r, c)])
    
    while q:
        x, y = q.popleft()
        if x == target[0] and y == target[1]:
            break

        for dx, dy in d:
            X = x + dx
            Y = y + dy
            if 0 <= X < l and 0 <= Y < l and visited[X][Y] == -1:
                visited[X][Y] = visited[x][y] + 1
                q.append((X, Y))
    
    return visited[target[0]][target[1]]

n = int(input())

for _ in range(n):
    l = int(input())
    cur = list(map(int, input().split()))
    target = list(map(int, input().split()))
    
    visited = [[-1] * l for _ in range(l)]
    visited[cur[0]][cur[1]] = 0
    print(BFS(cur[0], cur[1]))



        

