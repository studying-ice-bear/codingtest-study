import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr.sort()
# 두 포인터
start, end = 0, len(arr)-1
count = 0
S = 0  # sum
arr.sort()
while True:
    S = arr[start] + arr[end]

    if S == x:
        count += 1

    if S <= x:
        start += 1
    else:
        end -= 1

    if end <= start:
        break


print(count)
'''
input:
9
5 12 7 10 9 1 2 3 11
13

output:
3

input:
5
4 3 5 4 2
8
output:
2

input:
5
5 4 3 2 1
6
output:
2

input:
6
1 2 1 4 3 4
5
output:
3
'''