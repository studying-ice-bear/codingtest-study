"""
Dynamic Programming

아직 풀지 못함
"""

import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

memo = [[0, 0] for _ in range(n)]
if n >= 1:
    memo[0] = [wine[0], 0]
if n >= 2:
    memo[1] = [wine[1] + wine[0], wine[0]]
if n >= 3:
    memo[2] = [max(wine[2] + wine[1], wine[2] + wine[0]), wine[1] + wine[0]]
    for i in range(3, n):
        memo[i][0] = max(wine[i] + wine[i-1] + memo[i-2][1], memo[i-2][0] + wine[i])
        memo[i][1] = wine[i-1] + wine[i-2] + memo[i-3][1]
print(memo)
print(max(memo[n-1]))