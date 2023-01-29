import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
pick = list(map(int, sys.stdin.readline().split()))
# print(n, m, pick)

dq = deque(list(range(1, n + 1)))
# print(dq)

answer = 0
for i in range(m):
    if dq[0] != pick[i]:
        if dq.index(pick[i]) <= (len(dq) // 2):
            while dq[0] != pick[i]:
                dq.rotate(-1)
                answer += 1
        else:
            while dq[0] != pick[i]:
                dq.rotate(1)
                answer += 1
    if dq[0] == pick[i]:
        dq.popleft()

print(answer)
