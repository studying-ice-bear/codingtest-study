import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
distance = [0] * (MAX + 1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(distance[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                q.append(nx)

bfs()