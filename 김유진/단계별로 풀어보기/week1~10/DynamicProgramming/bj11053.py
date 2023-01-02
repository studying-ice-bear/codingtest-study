import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
'''
6
1 2 8 2 4 8
output:
4

5
5 1 2 3 4
output:
4
'''