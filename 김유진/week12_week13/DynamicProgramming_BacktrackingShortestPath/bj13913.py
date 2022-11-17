import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 10**5
distance = [0] * (MAX + 1)
move = [0] * (MAX + 1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(distance[x])
            arr = []
            temp = x
            for _ in range(distance[x]+1):
                arr.append(temp)
                temp = move[temp]
            print(' '.join(map(str, arr[::-1])))
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not distance[nx]: # distance는 초기값이 모두 0이므로 False, distance[nx] == 0
                distance[nx] = distance[x] + 1
                move[nx] = x
                q.append(nx)

bfs()