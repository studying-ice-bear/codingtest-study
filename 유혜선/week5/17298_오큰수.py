"""
- 스택

idea > stack에 stack에 있는 수보다 현재 수가 작은 경우 넣고, 큰 경우 차례대로 빼기

ex > arr = [3, 5, 2, 7]
stack = []
answer = [-1, -1, -1, -1]
i = 0
stack이 비었으므로 arr[i]를 stack에 넣기

stack = [3]
answer = [-1, -1, -1, -1]
i = 1
arr[i]가 stack[-1]보다 크므로 stack.pop() => pop한 값의 자리에 arr[i]를 넣기

stack = [5]
answer = [5, -1, -1, -1]
i = 2
arr[i]가 stack[-1]보다 작으므로 stack.append(arr[i])

stack = [5, 2]
answer = [5, -1, -1, -1]
i = 3
arr[i]가 stack[-1]보다 크므로 stack.pop() => pop한 값의 자리에 arr[i]를 넣기
answer = [5, -1, 7, -1]
stack = [5]
arr[i]가 stack[-1]보다 크므로 stack.pop() => pop한 값의 자리에 arr[i]를 넣기
answer = [5, 7, 7, -1]

stack = [7]
answer = [5, 7, 7, -1]
i == n이므로 끝!

"""
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = [-1] * n
stack = []
for i, val in enumerate(arr):
    if not stack:
        stack.append((val, i))
        continue

    while stack:
        if stack[-1][0] < val:
            idx = stack.pop()[1]
            answer[idx] = val
        else:
            break

    stack.append((val, i))


print(*answer)
  
