"""
- 동적계획법과 최단거리 역추적

idea 1.> dp로 1 ~ n까지 최소 횟수 모두 구한 후에, n ~ 1까지 다시 내려가면서 경로 출력
메모리 38652KB, 시간 720ms
"""

import sys
input = sys.stdin.readline
INF = int(10e9)
n = int(input())
memo = [False] * (n + 1)
memo[1] = 0

for i in range(2, n+1):
    temp = n
    if i % 3 == 0 and temp > memo[i // 3] + 1:
        temp = memo[i // 3] + 1
    
    if i % 2 == 0 and temp > memo[i // 2] + 1:
        temp = memo[i // 2] + 1
    
    if i > 1 and temp > memo[i - 1] + 1:
        temp = memo[i - 1] + 1
    
    memo[i] = temp

print(memo[n])

def tracking(cur):
    print(cur, end=" ")
    if cur == 1:
        return
    temp_val = cur
    temp_idx = cur
    if cur % 3 == 0 and temp_val > memo[cur // 3]:
        temp_val = memo[cur // 3]
        temp_idx = cur // 3
    
    if cur % 2 == 0 and temp_val > memo[cur // 2]:
        temp_val = memo[cur // 2]
        temp_idx = cur // 2
    
    if cur - 1 > 1 and temp_val > memo[cur - 1]:
        temp_val = memo[cur - 1]
        temp_idx = cur - 1
    
    tracking(temp_idx)

tracking(n)

"""
idea 2.> n부터 1까지 내려가면서 이전 경로를 visited에 저장 후 1부터 다시 올라가면서 경로 출력
-> BFS 느낌~
메모리 38756KB, 시간 92ms
""" 
from collections import deque as dq

def solution(n):
    visited = [0] * (n + 1)
    q = dq([n])
    visited[n] = n
    while q:
        cur = q.popleft()

        if cur == 1:
            break

        temp = []
        if cur % 3 == 0:
            temp.append(cur // 3)
        if cur % 2 == 0:
            temp.append(cur // 2)
        temp.append(cur - 1)

        for t in temp:
            if not visited[t]:
                visited[t] = cur
                q.append(t)
    start = 1
    route = [1]
    while True:
        if start == visited[start]:
            break
        route.append(visited[start])
        start = visited[start]
    
    print(len(route)-1)
    print(*sorted(route, reverse=True))
    return

solution(n)