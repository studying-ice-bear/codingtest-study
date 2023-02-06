from collections import deque
import sys

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)

for i in range(V):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]


def bfs(start=1):
    visited[start] = True
    que = deque([start])
    while que:
        node = que.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                que.append(i)


def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if not visited[nx]:
            dfs(nx)


bfs()
# dfs(1)
print(sum(visited) - 1)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
