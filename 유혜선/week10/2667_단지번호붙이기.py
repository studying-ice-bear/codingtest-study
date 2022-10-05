"""
- 그래프와 순회(DFS/BFS)

idea> 1인 곳을 찾아 DFS 혹은 BFS를 이용하여 개수 세기
- 개수 세고 나서는 확인한 집은 0으로 변환 (중복 방지)
"""
import sys
from collections import deque as dq
input = sys.stdin.readline

def solution_BFS():
    n = int(input())
    squared = [list(map(int, list(input().rstrip()))) for _ in range(n)]

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = []
    for i in range(n):
        for j in range(n):
            if squared[i][j] == 1:
                q = dq([(i, j)])
                cnt = 0
                while q:
                    r, c = q.popleft()
                    if squared[r][c] == 0:
                        continue
                    squared[r][c] = 0
                    cnt += 1
                    for k in range(4):
                        nr = r + d[k][0]
                        nc = c + d[k][1]
                        if 0 <= nr < n and 0 <= nc < n and squared[nr][nc] == 1:
                            q.append((nr, nc))
                answer.append(cnt)
    answer.sort()
    print(len(answer))
    print(*answer, sep="\n")
    return


def solution_DFS():
    n = int(input())
    squared = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(n):
            if squared[i][j] == 1:
                cnt = 0
                def DFS(r, c):
                    nonlocal cnt
                    squared[r][c] = 0
                    cnt += 1
                    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for k in range(4):
                        nr = r + d[k][0]
                        nc = c + d[k][1]
                        if 0 <= nr < n and 0 <= nc < n and squared[nr][nc] == 1:
                            DFS(nr, nc)
                DFS(i, j)
                answer.append(cnt)
    answer.sort()
    print(len(answer))
    print(*answer, sep="\n")
    return

solution_DFS()
