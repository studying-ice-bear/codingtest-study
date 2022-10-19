import sys

N = int(input())
A = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N
dp = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(N-1, -1, -1):
    for k in range(N - 1, i, -1):
        if A[i] > A[k]:
            dp2[i] = max(dp2[i], dp2[k] + 1)
    dp[i] = dp1[i] + dp2[i] - 1

# print(A)
# print(dp1)
# print(dp2)
# print(dp)
print(max(dp))
