import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

for i in range(N-1):
    for j in range(i):
        if arr[i][1] > arr[i+1][1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i][0] > arr[i+1][0]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)
