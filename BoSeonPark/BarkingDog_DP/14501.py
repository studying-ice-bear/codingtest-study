import sys
input = sys.stdin.readline

n = int(input())

schedule = []
dp = [0 for _ in range(n+1)]

for i in range(n):
    t, p = map(int, input().split())
    
    schedule.append([t, p])

for i in range(n-1, -1, -1):
    t, p = schedule[i]

    if i + t > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i+1], p + dp[i + t])

print(dp[0])
