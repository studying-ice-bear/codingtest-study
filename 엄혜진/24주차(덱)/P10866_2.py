import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

dq = deque()

answer = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if len(dq) > 0:
            answer.append(dq.popleft())
        else:
            answer.append(-1)
    elif command[0] == 'pop_back':
        if len(dq) > 0:
            answer.append(dq.pop())
        else:
            answer.append(-1)
    elif command[0] == 'size':
        answer.append(len(dq))
    elif command[0] == 'empty':
        if len(dq) > 0:
            answer.append(0)
        else:
            answer.append(1)
    elif command[0] == 'front':
        if len(dq) > 0:
            answer.append(dq[0])
        else:
            answer.append(-1)
    elif command[0] == 'back':
        if len(dq) > 0:
            answer.append(dq[-1])
        else:
            answer.append(-1)

print('\n'.join(map(str, answer)))
