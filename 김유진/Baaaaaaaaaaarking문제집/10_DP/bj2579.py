import sys
N = int(sys.stdin.readline())
stair = []
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

dp = [0] * N

if N == 1:
    print(stair[0])
elif N == 2:
    print(stair[0] + stair[1])
elif N == 3:
    print(max(stair[0] + stair[2], stair[1] + stair[2]))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1]+stair[2])

    for i in range(3, N):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[-1])

'''
문제 링크: https://www.acmicpc.net/problem/2579
[1]
[1, 0] [1, 1]
[1, 0, 1] [0, 1, 1]
[1, 1, 0, 1] [0, 1, 0, 1] [1, 0, 1, 1] [0, 1, 1, 1]

6
10
20
15
25
10
20

'''