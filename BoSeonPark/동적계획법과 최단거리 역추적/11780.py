import sys
import math
input = sys.stdin.readline

n,m = int(input()),int(input())
graph = [[math.inf]*(n+1) for _ in range(n+1)]
path = [[-1]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)
    path[a][b] = a


# 플로이드 실행
for k in range(1, n+1):
    graph[k][k] = 0
    path[k][k] = -1
    for i in range(1, n+1):
        for j in range(1, n+1):
            d = graph[i][k]+graph[k][j]
            if graph[i][j] > d:
                graph[i][j] = d
                path[i][j] = path[k][j]
            
for i in graph[1:]:
    for j in i[1:]:
        print(j if j != math.inf else 0, end=" ")
    print()


# 최단거리 역추적
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if path[i][j] == -1:
            print(0)
            continue
        
        v = j
        ans = []
        while True:
            if v==i:
                break
            ans.append(v)
            v = path[i][v]
        print(len(ans)+1,i,*ans[::-1])
        
# 최단 거리, 최단 경로 출력 
# for i in range(1, len(graph)):
#     print(graph[i][1:])

# print()
# for i in range(1, len(path)):
#     print(path[i][1:])