import sys
import heapq
input = sys.stdin.readline

n = int(input())

max_heap = []
min_heap = []

for i in range(n):
    a = int(input())
    if i % 2 == 0:
        heapq.heappush(max_heap, -a)
    else:
        heapq.heappush(min_heap, a)
    if len(min_heap) != 0:
        if -max_heap[0] > min_heap[0]:
            mx = -heapq.heappop(max_heap)
            mn = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -mn)
            heapq.heappush(min_heap, mx)
    print(-max_heap[0])
        