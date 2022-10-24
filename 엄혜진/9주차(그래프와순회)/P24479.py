import sys

sys.setrecursionlimit(10 ** 9)  # 재귀가 너무 많아서 런타임에러 발생했음. 재귀 한도를 늘림.

N, M, R = map(int, sys.stdin.readline().rstrip().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())  # 입력이 많아서 input() 대신에 sys.stdin.readline().rstrip()를 써야함.
    graph[u].append(v)
    graph[v].append(u)


# print(N, M, R, visited, graph)


def dfs(V, E, R):  # V의 필요성은 아직 모르겠음.
    visited[0] += 1  # 방문 순서를 계속 유지하면서 확인해야하기 때문에 visited[0]에 현재끼지 방문한 노드의 개수를 저장함.
    visited[R] = visited[0]
    for i in sorted(E[R]):  # 문제에서 오름차순으로 방문한다고 해서 정렬함.
        if visited[i] == 0:
            dfs(V, E, i)


dfs(N, graph, R)
print('\n'.join(map(str, visited[1:])))
