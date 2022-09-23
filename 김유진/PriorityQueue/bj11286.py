import sys, heapq
N = int(sys.stdin.readline())

absheap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(absheap, x)

    else:
        if not absheap:
            print(0)
        else:
            print(heapq.heappop(absheap)
