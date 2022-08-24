import sys
N, K = map(int, sys.stdin.readline().split())
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline())

arr = sorted(arr, reverse=True)
print(arr)