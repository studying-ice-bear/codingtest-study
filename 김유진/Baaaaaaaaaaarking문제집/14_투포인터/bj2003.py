import sys
N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
left, right = 0, 0
total = 0
answer = 0

while left <= right:
    if total < M:
        if right == len(arr):
            break
        total += arr[right]
        right += 1
    else:
        if total == M:
            answer += 1

        total -= arr[left]
        left += 1

print(answer)
