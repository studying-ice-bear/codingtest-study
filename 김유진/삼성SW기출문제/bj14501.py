import sys
N = int(sys.stdin.readline())
T = [0] * N     # 상담을 완료하는데 걸리는 기간
P = [0] * N     # 받을 수 있는 금액

for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T[i] = t
    P[i] = p

dp = [0] * (N+1)

# bottom up
for i in range(N):
    for j in range(i+T[i], N+1):
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]
    # print(dp)
print(dp[-1])

# top down
for i in range(N-1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

print(dp[0])

'''
N: 남은 일수
T: 상담을 완료하는데 걸리는 기간
P: 받을 수 있는 금액
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200


'''