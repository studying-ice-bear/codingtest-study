"""
- 최단 경로

idea> 다익스트라 알고리즘 사용하기
- 다익스트라는 heapq(우선순위 큐)를 이용
- 가중치가 작은 순서대로 확인하므로 큐에 튜플 형태의 원소를 넣을때는 가중치가 맨 앞으로 와야 함
- 이미 최소 가중치로 방문한 노드는 큐에 넣지 않도록 처리 (메모리 초과)
"""
import sys
import heapq as hq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
start = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(graph, start):
    visited = ["INF"] * (V+1)
    visited[start] = 0
    q = []
    hq.heappush(q, (0, start))
    while q:
        dist, u = hq.heappop(q)
        
        if visited[u] < dist:
            continue

        for v, vw in graph[u]:
            cost = dist + vw

            if visited[v] == "INF" or cost < visited[v]:
                visited[v] = cost
                hq.heappush(q, (cost, v))
    
    return visited

print(*dijkstra(graph, start)[1:], sep="\n")


    


