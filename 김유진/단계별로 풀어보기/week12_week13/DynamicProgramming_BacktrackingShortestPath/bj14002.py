import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]


for i in range(N):
    stack = []
    for j in range(i):
        if arr[j] < arr[i]:
            stack.append(arr[j])
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

length = max(dp)
result = []
for i in range(N-1, -1, -1):
    if dp[i] == length:
        result.append(arr[i])
        length -= 1
result.reverse()
print(*result, sep=' ')

'''
10
50 40 10 23 60 30 40 50 70 80
output:
4
50 60 70 80
'''