"""
- 최단 경로

idea> 플로이드-워셜 알고리즘 사용
- 모든 지점에서 다른 모든 지점까지 최단 경로를 구해야 하는 경우 사용
- 3중 for문 이용
- a -> k -> b 에 대한 모든 경우를 확인 후 최단경로 갱신

"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(10e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for _ in range(1, n+1):
    graph[_][_] = 0

def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            if k == i:
                continue
            for j in range(1, n+1):
                if k == j or i == j:
                    continue
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return

floyd()
for r in range(1, n+1):
    for c in range(1, n+1):
        if graph[r][c] == INF:
            print(0, end=" ")
        else:
            print(graph[r][c], end=" ")
    print()