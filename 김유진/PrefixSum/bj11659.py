'''
testcase
5 3
5 4 3 2 1
1 3
2 4
5 5

output:
12
9
1
'''

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum = 0
prefix_sum = [0]
for a in arr:
    sum += a
    prefix_sum.append(sum)

result = []

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])

# print(*result, sep='\n')