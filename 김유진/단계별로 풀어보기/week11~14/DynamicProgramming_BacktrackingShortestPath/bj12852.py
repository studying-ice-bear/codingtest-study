import sys
N = int(sys.stdin.readline())
answer = 0
dp = [[0, []] for _ in range(N+1)]

dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[N][0])
print(*reversed(dp[N][1]))

'''
for i in range(1, N+1):
    dp.append(i)

for i in range(2, N+1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3])
    if N % 2 == 0:
        dp[i] = min(dp[i], dp[i//2])
    dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[N]-1)

while N > 1:
    print(N, end="")
    if dp[N] == dp[N-1]+1:
        N = N-1
    elif N % 2 == 0 and dp[N] == (dp[N//2] + 1):
        N = N // 2
    elif N % 3 == 0 and dp[N] == (dp[N//3] +1):
        N = N // 3
'''