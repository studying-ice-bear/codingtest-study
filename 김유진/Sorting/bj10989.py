import sys
numTestCases = int(sys.stdin.readline())
print(numTestCases)
arr = [0] * 1001

for _ in range(numTestCases):
    num = int(input())
    # if num not in arr:

for i in range(numTestCases, 0, -1):
    for j in range(i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(numTestCases):
    print(arr[i])