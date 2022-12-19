import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

for a in combinations_with_replacement(arr, M):
    print(*a)

# ans = []
#
# def dfs(depth, idx, n, m):
#     if depth == m:
#         print(*ans)
#         return
#     for i in range(idx, n):
#         ans.append(arr[i])
#         dfs(depth+1, i, n, m)
#         ans.pop()
#
# dfs(0, 0, N, M)