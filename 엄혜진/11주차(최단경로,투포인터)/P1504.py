import heapq
import sys

INF = int(1e9)

N, E = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)

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

    return distance


one = dijkstra(1)
v_one = dijkstra(v1)
v_two = dijkstra(v2)

answer = min(one[v1] + v_one[v2] + v_two[N], one[v2] + v_two[v1] + v_one[N])
print(answer if answer < INF else -1)
