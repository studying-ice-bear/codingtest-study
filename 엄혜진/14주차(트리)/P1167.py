import sys

# 트리 구조를 파악 해야 하고, 트리의 지름을 구해야 한다.

V = int(sys.stdin.readline().rstrip())

tree = [[] for _ in range(V + 1)]
parent = [0 for _ in range(V + 1)]

for _ in range(V):
    edges = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(1, len(edges) - 2, 2):
        tree[edges[0]].append((edges[i], edges[i + 1]))  # 정점번호, 거리


# print(tree)


# 1 번 노드에서 가장 먼 노드를 찾고, 그 노드에서 가장 먼 노드를 찾아서 간선의 길이를 구하면 된다는데, 이게 왜 되는 건지 모르겠다.
# 일단 구현해 보기로...!
# 위 방식에 대한 증명을 설명한 블로그: https://blog.myungwoo.kr/112
# 이해가 완벽히 되지는 않았다...ㅠ


def dfs(start, graph):
    stack = []

    visited[start] = 0

    stack.append([start, 0])
    while stack:
        cur, cur_dis = stack.pop()
        for nex, nex_dis in graph[cur]:
            if visited[nex] == -1:
                visited[nex] = cur_dis + nex_dis
                stack.append([nex, cur_dis + nex_dis])


visited = [-1] * (V + 1)
dfs(1, tree)

start = visited.index(max(visited))
visited = [-1] * (V + 1)
dfs(start, tree)
print(max(visited))

# 81792KB	668ms