import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
# print(N, K)

# 너무 어렵다.. 감이 아예 잡히질 않는다...
# https://wook-2124.tistory.com/273 참조
# v - 1, v + 1, v * 2 의 모든 경우의 수를 확인해 보되, 중복 되는 경우를 제외 하고 확인 한다.

visited = [0 for _ in range(100001)]


def bfs(R, current):
    dq = deque()
    visited[R] = 1
    dq.append((R, current))
    while dq:
        # print(dq)
        v, depth = dq.popleft()

        if v == K:
            print(depth)
            break

        if 0 <= v - 1 < 100001 and visited[v - 1] == 0:
            visited[v - 1] = 1
            dq.append((v - 1, depth + 1))
        if 0 <= v + 1 < 100001 and visited[v + 1] == 0:
            visited[v + 1] = 1
            dq.append((v + 1, depth + 1))
        if 0 <= v * 2 < 100001 and visited[v * 2] == 0:
            visited[v * 2] = 1
            dq.append((v * 2, depth + 1))


bfs(N, 0)

# 33760KB	156ms
