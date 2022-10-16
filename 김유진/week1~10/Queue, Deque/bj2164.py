from collections import deque
import sys
N = int(sys.stdin.readline())
arr = deque([i for i in range(1, N+1)])
# print(arr)

for i in range(N-1):
    arr.popleft()
    n = arr.popleft()
    arr.append(n)
    # print(arr)

print(arr[0])