"""
Dynamic Programming
- 주어진 배열을 a라고 할때,
- (n-1)번째 까지 연속합이 최대인 값을 S(n-1) 이라고 하면
S(n) 는 (S(n-1) + a[n]) 과 a[n] 중 큰 값이다.
"""

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

memo = [0] * n
memo[0] = arr[0]

for i in range(1, n):
    memo[i] = max(memo[i-1] + arr[i], arr[i])

print(max(memo))