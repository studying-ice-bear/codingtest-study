from collections import deque

n = int(input())
k = int(input())
computers = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(k):
    n1, n2 = map(int, input().split())
    computers[n1][n2] = computers[n2][n1] = 1

def bfs(v):
    queue = deque([v])
    visited[v] = True
    count = 0
    while queue:
        v = queue.popleft()
        for i in range(1, n+1):
            if computers[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count

print(bfs(1))