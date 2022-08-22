import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

visited = [False for _ in range(N)]
arr = [0 for _ in range(M)]

def dfs(n, target_depth, cur_depth):
    if target_depth == cur_depth:
        for item in arr:
            sys.stdout.write(str(item) + " ")
        sys.stdout.write('\n')
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            arr[cur_depth] = i + 1
            dfs(n, target_depth, cur_depth + 1)
            visited[i] = False


dfs(N, M, 0)
