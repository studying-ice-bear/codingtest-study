import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

board = [[0] * (n + 1)]
dp = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    board.append([0] + list(map(int, input().split(' '))))


for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = board[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split(' '))
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])


"""
0 0 0 0 0
0 1 2 3 4
0 2 3 4 5
0 3 4 5 6
0 4 5 6 7


00 00 00 00 00
00 01 03 06 10
00 03 08 15 24
00 06 15 27 42
00 10 24 42 64
"""
