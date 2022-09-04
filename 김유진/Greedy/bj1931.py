import sys
N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])

print(arr)