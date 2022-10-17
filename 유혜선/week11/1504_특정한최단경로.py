"""
- 최단 경로

idea> 
> 다익스트라 알고리즘 사용하기
- 다익스트라는 heapq(우선순위 큐)를 이용
- 가중치가 작은 순서대로 확인하므로 큐에 튜플 형태의 원소를 넣을때는 가중치가 맨 앞으로 와야 함
- 이미 최소 가중치로 방문한 노드는 큐에 넣지 않도록 처리 (메모리 초과)

> 주어진 두 점을 반드시 방문하기
i, j를 방문해야하므로 
- case1. 1 ~ i + i ~ j + j ~ n
- case2. 1 ~ j + j ~ i + i ~ n
두 경우 중 작은 값이 최단 경로 
"""
import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
    visited = [INF] * (N + 1)
    visited[start] = 0
    q = []
    hq.heappush(q, (0, start))
    while q:
        w, node = hq.heappop(q)

        if visited[node] < w:
            continue

        for v, vw in graph[node]:
            cost = w + vw
            if cost < visited[v]:
                visited[v] = cost
                hq.heappush(q, (cost, v))

    return visited


INF = int(10e9)
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

i, j = map(int, input().split())


start_1 = dijkstra(1)   # 1부터 모든 정점까지 최단거리
start_i = dijkstra(i)   # i부터 모든 정점까지 최단거리
start_j = dijkstra(j)   # j부터 모든 정점까지 최단거리

case_1 = start_1[i] + start_i[j] + start_j[N]
case_2 = start_1[j] + start_j[i] + start_i[N]

answer = min(case_1, case_2)
print(answer if answer < INF else -1)