import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for a in map(list, product(arr, repeat = M)):
    print(*a, sep=' ')

'''
ans = []
def dfs(depth, n, m):
    if depth == m:
        print(*ans)
        return
    for i in range(n):
        ans.append(arr[i])
        dfs(depth+1, n, m)
        ans.pop()

dfs(0, N, M)

'''