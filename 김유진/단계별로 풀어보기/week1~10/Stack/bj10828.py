import sys
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    task = sys.stdin.readline().split()

    if task[0] == "push":
        stack.append(int(task[1]))

    elif task[0] == "pop":
        if len(stack) == 0:
            num = -1
        else:
            num = stack.pop()
        print(num)

    elif task[0] == "size":
        print(len(stack))

    elif task[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif task[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
