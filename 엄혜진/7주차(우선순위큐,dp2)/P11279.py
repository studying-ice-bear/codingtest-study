import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
hq = []

# 1. 45980KB	192ms
# for _ in range(N):
#     x = int(input().rstrip())
#     if x == 0:
#         if len(hq) < 1:
#             print(0)
#         else:
#             print(heapq.heappop(hq)[1])
#     else:
#         heapq.heappush(hq, (-x, x))

# 2. 36764KB	156ms
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if len(hq) < 1:
            print(0)
        else:
            print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -x)
