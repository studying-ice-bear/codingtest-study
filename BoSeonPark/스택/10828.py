import sys
input = sys.stdin.readline

stack = []

n = int(input())

for _ in range(n):
    command = input().strip()
    
    if command[0:4] == 'push':
        c, num = command.split(' ')
        num = int(num)
    else:
        c = command
    
    if c == 'push':
        stack.append(num)
    elif c == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])