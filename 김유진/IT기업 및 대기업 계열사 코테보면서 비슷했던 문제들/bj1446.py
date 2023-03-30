import sys, heapq
INF = int(1e9)

N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    print(q)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        print(dist, now)
        print(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > D:
        continue
    graph[start].append((end, length))

dijkstra(0)
print(distance[D])

'''
highway = [i for i in range(D+1)]
shortcut = []

for _ in range(N):
    shortcut.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    start, end, length = shortcut[i]
    if start == 0:
        highway[end] = min(highway[end], length)
    elif end > D:
        continue
    else:
        highway[end] = min(highway[end], highway[start]+length)
        print(end, highway[end])

        for j in range(end+1, D):
            highway[j] = highway[j-1]+1
        print(highway)

print(highway[D])
'''

'''
3 20
1 10 5 
2 10 1 
10 15 3


5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
{(0, 50): 10, (50, 100): 10, (100, 151): 10, (110, 140): 90}
10(0~50), 10(50~100), 70(남은 거리)

2 100
10 60 40 -> 60-10= 50, 40 -> 50-40 = 10
50 90 20 -> 90-50= 40, 20 -> 40-20 = 20
100 - 20 = 8 

'''
