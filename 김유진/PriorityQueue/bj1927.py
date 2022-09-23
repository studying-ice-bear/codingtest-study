import sys, heapq
N = int(sys.stdin.readline())

minheap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(minheap, x)
    else:
        if not minheap:
            print(0)
        else:
            print(heapq.heappop(minheap))