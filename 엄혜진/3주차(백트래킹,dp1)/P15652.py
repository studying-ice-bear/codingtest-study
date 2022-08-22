import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [0 for _ in range(M)]


def dfs(n, target_depth, cur_depth):
    if target_depth == cur_depth:
        for i in arr:
            sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
        return

    start = 1
    if cur_depth > 0:
        start = arr[cur_depth-1]
    for i in range(start, n + 1):
        arr[cur_depth] = i
        dfs(n, target_depth, cur_depth + 1)


dfs(N, M, 0)
