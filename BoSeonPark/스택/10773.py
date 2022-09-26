import sys
input = sys.stdin.readline

stack = []

k = int(input())

for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))