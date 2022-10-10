"""
- 그래프와 순회(DFS/BFS)

idea> DFS로 풀기 (인접 노드 방문은 내림차순)
- 재귀 방식은 RecursionError => sys.setrecursionlimit(int(10e9))
- stack 방식으로 풀이
=> stack이 메모리는 조금 쓰고 시간도 크게 차이 안남(더 빠른것 같기도)
"""
import sys
sys.setrecursionlimit(int(10e9))
input = sys.stdin.readline

n, m, r = map(int, input().split())

visited = [0] * (n+1)

connected = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

for idx in range(1, n+1):
    # connected[idx].sort()     # stack 사용시 오름차순 정렬
    connected[idx].sort(reverse=True)   # 재귀 사용시 내림차순 정렬
    

def DFS_stack(start):
    stack = [start]
    o = 0
    while stack:
        node = stack.pop()
        if visited[node] != 0:
            continue
        o += 1
        visited[node] = o

        for val in connected[node]:
            if visited[val] == 0:
                stack.append(val)
    
    return

o = 1
def DFS(node):
    global o  
    visited[node] = o
    o += 1
    for val in connected[node]:
        if visited[val] == 0:
            DFS(val)


DFS(r)
print(*visited[1:], sep="\n")