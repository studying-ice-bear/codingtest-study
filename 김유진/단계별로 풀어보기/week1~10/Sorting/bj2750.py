import sys
numTestCases = int(input())

arr = []
for i in range(numTestCases):
    num = int(sys.stdin.readline())
    arr.append(num)

for a in sorted(arr):
    print(a)