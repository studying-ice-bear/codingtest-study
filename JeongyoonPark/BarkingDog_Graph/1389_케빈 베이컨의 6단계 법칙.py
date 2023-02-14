import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
relationship = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    relationship[a][b] = relationship[b][a] = 1

def bfs(x):
    visited = [False] * (n+1)
    answer = 0
    queue = deque([(x,0)])
    visited[x] = True
    while queue:
        x, current_level = queue.popleft()
        for i in range(1, n+1):
            if relationship[x][i] == 1 and not visited[i]:
                visited[i] = True
                answer += current_level+1
                queue.append((i, current_level+1))
    return answer 


result = []
for j in range(1, n+1):
    result.append(bfs(j))
kevin_bacon = result.index(min(result))
print(kevin_bacon + 1)