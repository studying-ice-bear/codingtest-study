import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split(' '))

circle = [i for i in range(1, n + 1)]
answer = []
i = 0
while len(circle) != 0:
    i += (k % len(circle)) - 1
    i = i % len(circle)
    answer.append(circle.pop(i))

print('<', end='')    
for i in answer:
    if answer[-1] != i:
        print(i, end=', ')
    else:
        print(i, end='')
print('>', end='')