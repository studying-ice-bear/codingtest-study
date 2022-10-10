import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) # 재귀허용 깊이 늘려주는 코드 *필수*
def dfs(v, g, r):
    global cnt
    
    v[r] = cnt
    for i in g[r]:
        if v[i] == 0:
            cnt += 1
            dfs(v, g, i)

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
        graph[i].sort()

dfs(visited, graph, r)

for i in range(1, n + 1):
    print(visited[i])