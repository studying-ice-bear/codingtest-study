import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
hq = []

for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if len(hq) < 1:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)

# 36764KB	164ms