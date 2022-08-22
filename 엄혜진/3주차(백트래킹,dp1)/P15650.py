import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [0 for _ in range(M)]


def dfs(n, start_n, target_depth, cur_depth):
    if target_depth == cur_depth:
        for i in arr:
            sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
        return

    for i in range(start_n, n + 1):
        arr[cur_depth] = i
        dfs(n, i + 1, target_depth, cur_depth + 1)


dfs(N, 1, M, 0)

# 코드가 이해는 되는데 이걸 아무것도 안보고 풀 수 있을까?
