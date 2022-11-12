import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

parent = [0] * (N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if parent[next] == 0:
                parent[next] = now
                queue.append(next)
bfs()
result = parent[2:]
print(*result, sep='\n')