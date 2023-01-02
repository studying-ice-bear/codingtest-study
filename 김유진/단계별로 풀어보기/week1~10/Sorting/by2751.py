import sys
numTestCases = int(sys.stdin.readline())

arr = []
for i in range(numTestCases):
    num = int(sys.stdin.readline())
    arr.append(num)

for num in sorted(arr):
    print(num)