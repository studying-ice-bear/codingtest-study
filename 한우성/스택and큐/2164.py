import sys
from collections import deque

N = int(sys.stdin.readline())
N_list = deque([x for x in range(1, N+1)])

while len(N_list) > 1:
    N_list.popleft()
    N_list.append(N_list.popleft())

print(N_list[0])