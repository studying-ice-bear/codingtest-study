import sys
import math
import heapq
input = sys.stdin.readline

def dijkstra(s):
    dp[s] = 0
    heapq.heappush(heap, [0, s])
    
    while heap:
        cur_w, cur_n = heapq.heappop(heap)
        
        if dp[cur_n] < cur_w:
            continue
        
        for c, w in graph[cur_n]:
            next_w = w + cur_w
            if next_w < dp[c]:
                dp[c] = next_w
                heapq.heappush(heap, [next_w, c])
                z
        

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
dp = [math.inf] * (v + 1)
heap = []

for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(k)
for i in range(1, v + 1):
    if dp[i] == math.inf:
        print('INF')
    else:
        print(dp[i])