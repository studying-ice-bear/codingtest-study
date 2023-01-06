import sys, math
N, M = map(int, sys.stdin.readline().strip().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
left, right = 0, 0
can = math.inf

while left < N and right < N:
    diff = abs(arr[left]-arr[right])
    # print(left, right, diff)

    if diff < M:
        right += 1
    else:
        can = min(can, diff)
        left += 1

print(can)

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