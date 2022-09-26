"""
- 그리디

idea > 순차적으로 주유소에 방문해서 가격이 낮은 주유소를 기준으로 계산
"""

import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
prices = list(map(int, input().split()))

total = d[0] * prices[0]
prev = prices[0]
for i in range(n-1):
    cur = prices[i]
    if prev < cur:
        cur = prev
    
    total += cur * d[i]
    prev = cur

print(total)