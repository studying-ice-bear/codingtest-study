import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())
visited = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# print(N, M, V, visited, graph)

# 1. dfs
answer = []


def dfs(E, R):
    visited[R] = 1
    answer.append(R)

    for i in sorted(E[R]):
        if visited[i] == 0:
            dfs(graph, i)


dfs(graph, V)
print(' '.join(map(str, answer)))

# 2. bfs
dq = deque()
answer = []


def bfs(E, R):
    dq.append(R)
    visited[R] = 1
    answer.append(R)

    while len(dq) > 0:
        u = dq.popleft()
        for v in sorted(E[u]):
            if visited[v] == 0:
                dq.append(v)
                visited[v] = 1
                answer.append(v)


count = 0
visited = [0 for _ in range(N + 1)]
bfs(graph, V)
print(' '.join(map(str, answer)))

# 32440KB	100ms
# 문제를 잘 못 이해했다. 노드 순서대로 출력하는 것이 아니라 탐색 순으로 출력하는 것임.