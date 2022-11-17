import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, N
arr.sort()
answer = 100000

# 연속된 수들의 부분합
while left <= right:
    if right < N:
        break

    if S <= sum(arr[left:right]):
        answer = (right-left) if answer > (right - left) else answer

    if S > sum(arr[left:right]):
        right -= 1
    else:
        left += 1

print(answer)