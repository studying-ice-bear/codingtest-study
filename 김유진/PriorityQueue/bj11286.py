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
            print(heapq.heappop(absheap))

'''
import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
'''
