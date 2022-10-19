import sys
from collections import deque

input = sys.stdin.readline

def bfs(v, g, r):
    global cnt
    
    v[r] = cnt
    queue = deque([r])
    
    while queue:
        pos = queue.popleft()
        for p in g[pos]:
            if v[p] == 0:
                cnt += 1
                v[p] = cnt
                queue.append(p)
    
            

n, m, r = map(int, input().split())

visited = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
cnt = 1
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n + 1):
    if len(graph[i]) >= 2:
        graph[i].sort(reverse=True)


bfs(visited, graph, r)

for i in range(1, n + 1):
    print(visited[i])
