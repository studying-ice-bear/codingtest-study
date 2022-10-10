import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
R = 1

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# print(N, M, R, graph, visited)

# 1. dfs (30840KB	68ms)
# count = 0
#
#
# def dfs(E, R):
#     global count
#
#     count += 1
#     visited[R] = count
#
#     for i in sorted(E[R]):
#         if visited[i] == 0:
#             dfs(graph, i)
#
#
# dfs(graph, R)
# print(count - 1) # 1번 컴퓨터 제외

# 2. bfs (32436KB	88ms)
dq = deque()
count = 0


def bfs(E, R):
    global count

    count += 1
    visited[R] = count
    dq.append(R)

    while len(dq) > 0:
        # print(dq)
        u = dq.popleft()
        for v in sorted(E[u]):
            if visited[v] == 0:
                dq.append(v)
                count += 1
                visited[v] = count



bfs(graph, R)
# print(visited)
print(count - 1)
