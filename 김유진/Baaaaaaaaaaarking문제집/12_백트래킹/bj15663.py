import sys
N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans = []
def dfs(depth, n, m):
    if depth == m:
        print(*ans)
        return
    for i in range(depth, n):
        ans.append(arr[i])
        dfs(i+1, n, m)
        ans.pop()

dfs(0, N, M)
