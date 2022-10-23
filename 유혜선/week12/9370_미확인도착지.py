"""
- 최단 경로

idea> 특정 경로를 지나는 다익스트라 알고리즘 사용하기
인접 행렬 방식 => 65132KB, 1720ms
인접 리스트 방식 => 44172KB, 444ms
"""

import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
    costs = [INF] * (n+1)
    q = [(0, start)]
    costs[start] = 0
    while q:
        dist, node = hq.heappop(q)
        if costs[node] < dist:
            continue

        for idx, val in enumerate(graph[node]):
            if val != 0:
                temp = dist + val
                if costs[idx] > temp:
                    costs[idx] = temp
                    hq.heappush(q, (temp, idx))
    return costs

T = int(input())
for i in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[0] * (n+1) for _ in range(n+1)]
    INF = int(10e9)

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a][b] = d
        graph[b][a] = d

    x_arr = [int(input()) for _ in range(t)]

    s_to = dijkstra(s)
    g_to = dijkstra(g)
    h_to = dijkstra(h)

    s_h = s_to[g] + g_to[h]
    s_g = s_to[h] + h_to[g]
    answer = []
    for x in x_arr:
        s_g_h_x = s_h + h_to[x]
        s_h_g_x = s_g + g_to[x]
        s_x = s_to[x]

        if s_x != INF and (s_g_h_x == s_x or s_h_g_x == s_x):
            answer.append(x)
    answer.sort()
    print(*answer, sep=" ")


"""
 def dijkstra(start):
    costs = [INF] * (n+1)
    q = [(0, start)]
    costs[start] = 0
    while q:
        dist, node = hq.heappop(q)
        if costs[node] < dist:
            continue

        for idx, val in graph[node]:
            if val != 0:
                temp = dist + val
                if costs[idx] > temp:
                    costs[idx] = temp
                    hq.heappush(q, (temp, idx))
    return costs

T = int(input())
for i in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    INF = int(10e9)

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    x_arr = [int(input()) for _ in range(t)]

    s_to = dijkstra(s)
    g_to = dijkstra(g)
    h_to = dijkstra(h)

    s_h = s_to[g] + g_to[h]
    s_g = s_to[h] + h_to[g]
    answer = []
    for x in x_arr:
        s_g_h_x = s_h + h_to[x]
        s_h_g_x = s_g + g_to[x]
        s_x = s_to[x]

        if s_x != INF and (s_g_h_x == s_x or s_h_g_x == s_x):
            answer.append(x)
    answer.sort()
    print(*answer, sep=" ")
 """   
