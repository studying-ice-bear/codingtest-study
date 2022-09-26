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
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(x), x))

# 39052KB	180ms