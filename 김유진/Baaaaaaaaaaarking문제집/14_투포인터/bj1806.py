import sys
N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))

left, right = 0, 0
total = 0
min_length = sys.maxsize

while True:
    if total >= S:
        min_length = min(min_length, right-left)
        total -= numbers[left]
        left += 1
    elif right == N:
        break
    else:
        total += numbers[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
        