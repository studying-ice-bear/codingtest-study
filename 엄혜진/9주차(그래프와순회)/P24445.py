import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, sys.stdin.readline().rstrip().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# print(N, M, R, visited, graph)

dq = deque([])
current = 1

def bfs(V, E, R):
    global current

    visited[R] = current
    current += 1
    dq.append(R)

    while len(dq) > 0:
        # print(visited, dq)
        u = dq.popleft()
        for v in sorted(E[u], reverse=True):
            if visited[v] == 0:
                visited[v] = current
                current += 1
                dq.append(v)

bfs(N, graph, R)
print('\n'.join(map(str, visited[1:])))

# 65716KB	676ms