"""
- 그래프와 순회(DFS/BFS)

idea> DFS로 풀기 (인접 노드 방문은 오름차순)
- 재귀 방식은 RecursionError
- stack 방식으로 풀이
"""
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

visited = [0] * (n+1)

connected = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

# def DFS_recursive(node, o):
#     visited[node] = o

#     connected[node].sort()
#     for t in connected[node]:
#         if not visited[t]:
#             DFS(t, o+1)
#     return

def DFS(start):
    stack = [start]
    o = 0
    while stack:
        node = stack.pop()
        if visited[node] != 0:
            continue
        o += 1
        visited[node] = o

        connected[node].sort(reverse=True)
        for t in connected[node]:
            if visited[t] == 0:
                stack.append(t)
        
    return


DFS(r)
print(connected)
print(*visited[1:], sep="\n")


        
