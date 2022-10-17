"""
- 최단 경로

idea> 
> 다익스트라 알고리즘 사용하기
- 다익스트라는 heapq(우선순위 큐)를 이용
- 가중치가 작은 순서대로 확인하므로 큐에 튜플 형태의 원소를 넣을때는 가중치가 맨 앞으로 와야 함
- 이미 최소 가중치로 방문한 노드는 큐에 넣지 않도록 처리 (메모리 초과)
=> 시간이 꽤 많이 걸림

> 0-1 너비우선탐색 알고리즘 사용하기
- 순간이동 하는 경우 deque의 앞에 넣어줌
"""
import sys
import heapq as hq
input = sys.stdin.readline


n, k = map(int, input().split())
INF = int(10e9)
l = max(n, k)
visited = [INF] * (2*l + 1)

def dijkstra(start):
    visited[start] = 0

    q = []
    hq.heappush(q, (0, start))

    while q:
        t, idx = hq.heappop(q)

        if visited[idx] < t:
            continue
        
        for next_idx, dt in [(idx + 1, 1), (idx - 1, 1), (2 * idx, 0)]:
            if 0 <= next_idx <= 2 * l:
                cost = t + dt
                if cost < visited[next_idx]:
                    visited[next_idx] = cost
                    hq.heappush(q, (cost, next_idx))
    
    return visited

arr = dijkstra(n)
print(visited)
print(visited[k])


