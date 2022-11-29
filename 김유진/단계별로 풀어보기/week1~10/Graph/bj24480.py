import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)
current = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort(reverse=True)

def dfs(v):
    global current
    answer[v] = current
    for to_v in graph[v]:
        if answer[to_v]:
            continue
        current += 1
        dfs(to_v)

dfs(r)
print(*answer[1:], sep='\n')
