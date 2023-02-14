from collections import deque
import sys

MAX = 10 ** 5
N, K = map(int, sys.stdin.readline().split())

dist = [0] * (MAX+1)

que = deque([N])
while que:
    x = que.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX and not dist[nx]:
            dist[nx] = dist[x]+1
            que.append(nx)

