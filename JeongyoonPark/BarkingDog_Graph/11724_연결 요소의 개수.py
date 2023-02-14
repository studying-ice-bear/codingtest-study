import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in range(1,n+1):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

if m == 0:
    count = n
else:
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            count += 1

print(count)

'''
반례
6 0

답: 6
'''