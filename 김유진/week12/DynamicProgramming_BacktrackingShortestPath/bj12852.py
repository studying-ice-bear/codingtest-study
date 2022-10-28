import sys
N = int(sys.stdin.readline())
answer = 0
dp = []

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