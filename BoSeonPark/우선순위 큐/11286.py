import sys
import heapq
input = sys.stdin.readline

n = int(input())

nums = []

for i in range(n):
    a = int(input())
    if len(nums) == 0 and a == 0:
        print(0)
    elif a == 0:
        print(heapq.heappop(nums)[1])
    else:
        heapq.heappush(nums, (abs(a), a))