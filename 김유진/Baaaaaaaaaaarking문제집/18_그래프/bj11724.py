import sys
# sys.setrecursionlimit(5000)
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start, depth):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N+1)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            # dfs(i, 0)
            bfs(i)
            count += 1

print(count)

'''
https://ji-gwang.tistory.com/292
'''
