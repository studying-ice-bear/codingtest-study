from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    task = list(sys.stdin.readline().split())

    if task[0] == "push":
        queue.append(task[1])
    elif task[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif task[0] == "size":
        print(len(queue))
    elif task[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif task[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif task[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])