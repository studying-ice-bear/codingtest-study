import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
stack = []
count = 0

for i in arr: # [10, 3, 7, 4, 12, 2]
    while stack and stack [-1] <= i:
            stack.pop()
    stack.append(i)
    count += len(stack) - 1

print(count)

