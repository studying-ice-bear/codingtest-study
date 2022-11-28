import sys
N, K = map(int, sys.stdin.readline().split())
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline())

arr = sorted(arr, reverse=True)
count = 0

for i in range(N):
    count += K // arr[i]
    K = K % arr[i]

print(count)
