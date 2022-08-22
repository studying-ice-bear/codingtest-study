"""
-Backtracking

- idea 1> DFS로 풀기
DFS를 이용하여 방문처리 t/f 여부로 팀을 구성한 후 (종료 조건 : dfs 깊이 = n // 2)
종료조건을 만족하면 팀을 바탕으로 능력치를 계산하여 최소값 갱신

- idea 2> 조합으로 풀기
itertools의 combinations 모듈을 이용하여 가능한 조합을 구한 뒤
해당 조합에서 2개씩 뽑는 조합을 다시 추출하여 팀별 능력치를 계산하고 최소값 갱신
=> 능력치를 저장하기 위해선 같은 팀 두명(i, j)이 필요함
=> 조합 1 (n명의 사람 중 n // 2명 순서 없이 뽑기) -> 조합 2 (n // 2 명의 사람 중 2명 순서 없이 뽑기)

조합으로 풀 경우 (1, 2), (3, 4) 인 경우와 (3, 4), (1, 2) 인 경우가 동일하다고 봐도 되므로
모든 조합을 보지 않고 절반만 봐도 됨
"""
import sys
from itertools import combinations as cb
input = sys.stdin.readline

# 입력값 (n: 축구에 참여하는 인원수, arr[i][j]: 선수 i와 j가 같은 팀일때 더해지는 능력치 리스트)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# idea 1> DFS로 풀기
# visited = [False] * n
# min_val = 100

# def DFS(cnt, x):
#     global min_val
#     print("---")
#     if cnt == n//2:
#         START, LINK = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if visited[i] and visited[j]:
#                     START += arr[i][j]
#                 elif not visited[i] and not visited[j]:
#                     LINK += arr[i][j]

#                 else:
#                     continue
#         min_val = min(min_val, abs(START - LINK))
#         return
    
#     else:
#         for dx in range(x, n):
#             if not visited[dx]:
#                 visited[dx] = True
#                 DFS(cnt + 1, dx)
#                 visited[dx] = False
    
# visited[0] = True
# DFS(1, 1)
# print(min_val)
    

# idea 2> 조합으로 풀기
def solution2(n, arr):
    min_val = 100

    combis = list(cb(range(n), n//2))
    l = len(combis)
    for k in range(l//2):
        combi = combis[k]
        START = combi
        LINK = [i for i in range(n) if i not in START]

        start_val = 0
        link_val = 0
        for a, b in cb(START, 2):
            start_val += arr[a][b] + arr[b][a]
        
        for c, d in cb(LINK, 2):
            link_val += arr[c][d] + arr[d][c]

        if abs(start_val - link_val) < min_val:
            min_val = abs(start_val - link_val)
    
    return min_val


print(solution2(n, arr))
