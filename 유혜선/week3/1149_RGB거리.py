"""
Dynamic Programming
- 참고: https://zidarn87.tistory.com/272

"""

import sys
input = sys.stdin.readline

n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]
memo = [[0, 0, 0] for _ in range(n)]

memo[0] = houses[0]

for i in range(1, n):
    memo[i][0] = houses[i][0] + min(memo[i-1][1], memo[i-1][2])
    memo[i][1] = houses[i][1] + min(memo[i-1][0], memo[i-1][2])
    memo[i][2] = houses[i][2] + min(memo[i-1][0], memo[i-1][1])

print(memo)
print(min(memo[n-1]))

"""
- Backtracking 풀이 (시간초과)
INF = int(10e9)
min_val = INF
def BT(idx, color, total):
    global n, min_val
    if idx == n:
        if min_val > total:
            min_val = total
        return

    for i, val in enumerate(houses[idx]):
        if i != color:
            total += val
            BT(idx+1, i, total)
            total -= val


BT(0, 0, 0)
BT(0, 1, 0)
BT(0, 2, 0)

print(min_val)
"""  
