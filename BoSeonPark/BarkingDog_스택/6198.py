import sys
input = sys.stdin.readline

n = int(input())
answer = 0
stack = []
building = [int(input()) for _ in range(n)]

for i in range(n):
    while stack:
        if stack[-1] <= building[i]:
            stack.pop()
        else:
            break
    stack.append(building[i])
    answer += len(stack) - 1
print(answer)