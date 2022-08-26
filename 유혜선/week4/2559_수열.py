"""
- 누적합
k개 부분합의 최댓값을 구하는 문제
반복문의 범위를 (k, n+1)로 설정 (부분합 맨 처음에 0을 넣어줬음)
"""

import sys
from itertools import accumulate
input = sys.stdin.readline

n, k = map(int, input().split())
acc = [0] + list(accumulate(map(int, input().split())))

max_val = -int(10e9)
for i in range(k, n+1):
    if acc[i] - acc[i-k] > max_val:
        max_val = acc[i] - acc[i-k]

print(max_val)