import sys
sys.setrecursionlimit(10**6)    # 재귀 허용 깊이를 수동으로 늘려주는 코드

# N: 정점의 수, M: 간선의 수, R: 시작 정점
N, M, R = map(int, sys.stdin.readline().split())
graph = [[]*(N+1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
for i in range(N+1):
    graph[i].sort()

visited = [-1] * (N + 1)
result = [0] * (N+1)
cnt = 0
# V: 정점 집합, E: 간선 집합, R: 시작 정점
def dfs(E, R):
    global cnt
    cnt += 1
    visited[R] = 1
    result[R] = cnt

    for x in E[R]:
        if visited[x] == -1:
            dfs(E, x)

dfs(graph, 1)
print(*result[1:], sep='\n')

'''
4 4 1
1 2
1 3
1 4
2 4
'''
