import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [0 for _ in range(M)]


def dfs(n, target_depth, cur_depth):
    if target_depth == cur_depth:
        for i in arr:
            sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
        return

    for i in range(n):
        arr[cur_depth] = i + 1
        dfs(n, target_depth, cur_depth + 1)


dfs(N, M, 0)

# 코드 작성하고 바로 돌리지 말고 머리속으로 다시 톺아보는 습관을 들이자
