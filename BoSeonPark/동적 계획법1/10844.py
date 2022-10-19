import sys
input = sys.stdin.readline

n = int(input())

dp = [[1]+[0]*10 for _ in range(101)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 10):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])

for i in range(n+1):
    print(dp[i])
print(sum(dp[n][:10]) % 1000000000)


# n = int(input())
# dp = [[0 for i in range(10)] for j in range(101)]
# for i in range(1, 10):
#     dp[1][i] = 1
# for i in range(2, n + 1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i - 1][1]
#         elif j == 9:
#             dp[i][j] = dp[i - 1][8]
#         else:
#             dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# for i in range(n+1):
#     print(dp[i])
# print(sum(dp[n]) % 1000000000)
# N = int(input())
# dp = [[0]*10 for _ in range(N+1)]
# for i in range(1, 10):
#     dp[1][i] = 1

# MOD = 1000000000

# for i in range(2, N+1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i-1][1]
#         elif j == 9:
#             dp[i][j] = dp[i-1][8]
#         else:
#             dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

# for i in range(N+1):
#     print(dp[i])
# print(sum(dp[N]) % MOD)
