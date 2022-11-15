import sys

n = int(sys.stdin.readline().rstrip())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p_v, c_v, e = map(int, sys.stdin.readline().rstrip().split())
    tree[p_v].append((c_v, e))
    tree[c_v].append((p_v, e))


# print(tree)


def dfs(start, graph):
    stack = []
    stack.append([start, 0])
    visited[start] = 0
    while stack:
        cur, cur_dis = stack.pop()
        for nex, nex_dis in graph[cur]:
            if visited[nex] == -1:
                visited[nex] = cur_dis + nex_dis
                stack.append([nex, cur_dis + nex_dis])


visited = [-1] * (n + 1)
dfs(1, tree)

start_idx = visited.index(max(visited))
visited = [-1] * (n + 1)
dfs(start_idx, tree)

print(max(visited))

# 33908KB	108ms