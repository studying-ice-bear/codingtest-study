import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

visited = [False] * N
result = [0] * M
def dfs(x):
    if x == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            result[x] = i+1
            visited[i] = True
            dfs(x+1)
            visited[i] = False

dfs(0)