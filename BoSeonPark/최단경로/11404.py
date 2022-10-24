import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [[math.inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)

for j in range(1, n+1):
    for i in range(1, n+1):
        for k in range(1, n+1):
            if i == k:
                dp[i][k] = 0
            else:
                dp[i][k] = min(dp[i][j] + dp[j][k], dp[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(dp[i][j], end=' ')
    print('')