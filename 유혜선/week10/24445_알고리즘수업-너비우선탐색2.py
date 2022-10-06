"""
- 그래프와 순회(DFS/BFS)

idea> BFS로 풀기 (인접 노드 방문은 오름차순)
- Q 이용
- connected를 2차원 배열로 하면 더 빠름
"""
import sys
from collections import deque as dq
input = sys.stdin.readline

n, m, r = map(int, input().split())
connected = {i: [] for i in range(1, n+1)}
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

for idx in range(1, n+1):
    connected[idx].sort(reverse=True)

def BFS(start):
    q = dq([start])
    o = 1
    while q:
        node = q.popleft()
        if visited[node] != 0:
            continue
        visited[node] = o
        o += 1
        for val in connected[node]:
            if visited[val] == 0:
                q.append(val)
    
    return

BFS(r)
print(*visited[1:], sep="\n")