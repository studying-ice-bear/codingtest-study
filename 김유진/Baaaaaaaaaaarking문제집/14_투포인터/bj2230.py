import sys
N, M = map(int, sys.stdin.readline().strip().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
left, right = 0, len(arr)-1
can = []

while left < right:
    diff = abs(arr[left]-arr[right])
    print(left, right, diff)

    if diff > M:
        can.append(diff)
        right -= 1
        left += 1
    elif diff == M:
        can.append(diff)
        break
    else:
        left -= 1

print(min(can))

'''
3 3
1
5
3

5 6
1
2
3
4
11
'''