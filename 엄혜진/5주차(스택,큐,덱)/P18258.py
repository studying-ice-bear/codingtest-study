import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()
for _ in range(n):
    line = sys.stdin.readline().rstrip().split()
    action = ""
    x = 0
    if len(line) > 1:
        action = line[0]
        x = int(line[1])
    else:
        action = line[0]

    if action == "push":
        q.append(x)
    elif action == "pop":
        if len(q) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(q.popleft()) + '\n')
    elif action == "size":
        sys.stdout.write(str(len(q)) + '\n')
    elif action == "empty":
        if len(q) == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif action == "front":
        if len(q) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(q[0]) + '\n')
    elif action == "back":
        if len(q) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(q[len(q) - 1]) + '\n')
# 110064KB	2408ms

# [deque](https://docs.python.org/3/library/collections.html?highlight=deque#collections.deque)
# append(x)
# appendleft(x)
# clear()
# copy()
# count(x)
# extend(iterable)
# extendleft(iterable)
# index(x[, start[, stop]]) # New in version 3.5.
# insert(i, x) # New in version 3.5.
# pop()
# popleft()
# remove(value)
# reverse() # New in version 3.2.
# rotate(n=1) # Rotate the deque n steps to the right. If n is negative, rotate to the left.
# When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).

# read-only attribute:
# maxlen # Maximum size of a deque or None if unbounded. # New in version 3.1.
