import sys, heapq
N = int(sys.stdin.readline())

maxheap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(maxheap, -1 * x)
    else:
        if not maxheap:
            print(0)
        else:
            print(-1* heapq.heappop(maxheap))