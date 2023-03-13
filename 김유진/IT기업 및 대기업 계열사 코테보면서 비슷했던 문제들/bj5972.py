import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y, a = map(int, sys.stdin.readline().split())
    graph[x].append((y, a))
    graph[y].append((x, a))

INF = int(1e9)

distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

print(distance[-1])
