import sys

sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, sys.stdin.readline().rstrip().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)


# print(N, M, R, visited, graph)


def dfs(V, E, R):
    visited[0] += 1
    visited[R] = visited[0]
    for i in sorted(E[R], reverse=True):
        if visited[i] == 0:
            dfs(V, E, i)


dfs(N, graph, R)
print('\n'.join(map(str, visited[1:])))
