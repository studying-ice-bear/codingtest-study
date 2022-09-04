import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefix = []
sum = 0

for a in arr:
    sum += a
    prefix.append(sum)

prefix_sum = []

prefix_sum.append(prefix[K-1])
for i in range(1, N-K+1):
    prefix_sum.append(prefix[i+K-1] - prefix[i-1])

print(max(prefix_sum))


'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3
[3, 1, -3, -12, -12, -9, -2, 11, 19, 16]
'''