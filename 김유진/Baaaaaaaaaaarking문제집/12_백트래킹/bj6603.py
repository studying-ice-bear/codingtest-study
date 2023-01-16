import sys
from itertools import combinations

while True:
    arr = list(map(int, sys.stdin.readline().strip().split()))
    k, S = arr[0], arr[1:]
    if k == 0:
        exit()

    for p in map(list, combinations(S, 6)):
        print(*p)
    print()



'''
arr = []
ans = [0] * 6
def dfs(start, depth):
    if depth == 6:
        print(*ans)
        return
    for i in range(start, k):
        ans[depth] = S[i]
        dfs(i+1, depth+1)

while len(arr) != 1:
    arr = list(map(int, sys.stdin.readline().strip().split()))
    k = arr[0]
    S = arr[1:]
    dfs(0, 0)
    print()
'''