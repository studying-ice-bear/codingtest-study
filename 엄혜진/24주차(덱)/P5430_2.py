import sys
from collections import deque

answer = []
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline()[1:-2].split(',')
    if n > 0:
        dq = deque(list(map(int, arr)))
    else:
        dq = deque()
    # print(p, n, dq)

    head_is_top = True
    error = False
    for i in range(len(p)):
        if p[i] == 'R':
            head_is_top = False if head_is_top else True
        elif p[i] == 'D':
            if len(dq) > 0:
                dq.popleft() if head_is_top else dq.pop()
            else:
                answer.append('error')
                error = True
                break

    if not error:
        if head_is_top:
            answer.append('[' + ','.join(map(str, dq)) + ']')
        else:
            answer.append('[' + ','.join(map(str, reversed(dq))) + ']')

print('\n'.join(answer))
