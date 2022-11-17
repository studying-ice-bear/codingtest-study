import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, len(arr)-1
arr.sort()
sub = 2000000000    # 1000000000, 1000000000인 경우
answer = []
while True:
    if left >= right:
        break

    S = abs(arr[left] + arr[right])

    if sub >= S:
        sub = S
        answer = [arr[left], arr[right]]

    if abs(arr[left]) >= abs(arr[right]):
        left += 1
    else:
        right -= 1

print(*answer, sep=' ')

'''
input:
5
-1 -2 2 0 99
output:
-2 2

2
1000000000 1000000000


'''