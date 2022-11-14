import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))

# import sys
#
# n = int(sys.stdin.readline())  # 노드의 개수
# graph = [[] for _ in range(n + 1)]
#
# # 부모 노드의 번호, 자식 노드, 간선의 가중치
# # 루트 노드의 번호는 항상 1
# # 간선의 가중치는 100보다 크지 않은 양의 정수
#
# 핵심 아이디어
# 루트에서 가장 거리가 먼 점 t가 만약 지름 안에 있다면,
# t에서 가장 거리가 먼 점 u까지가 지름이다.
# 귀류법으로 증명한 블로그 https://koosaga.com/14
#
# for _ in range(n - 1):
#     parent, son, weight = map(int, sys.stdin.readline().strip().split())
#     graph[parent].append([son, weight])
#     graph[son].append([parent, weight])
#
# # print(graph)
#
# distance = [-1] * (n + 1)
# distance[1] = 0
#
#
# def dfs(node, weight):
#     for i in graph[node]:
#         son, son_weight = i
#         if distance[son] == -1:
#             distance[son] = weight + son_weight
#             dfs(son, weight + son_weight)
#
#
# # 루트 노드에서 가장 먼 곳을 찾는다.
# distance = [-1] * (n + 1)
# distance[1] = 0
# dfs(1, 0)
#
# # 위에서 찾은 노드에 대한 가장 먼 노드
# start = distance.index((max(distance)))
#
# # 그 노드에서 다시 먼 노드를 찾는다.
# distance[start] = 0
# dfs(start, 0)
#
# print(max(distance))
