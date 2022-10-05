"""
- 그래프와 순회(BFS)

idea> 토마토 3차원 버전
- bfs 이용
- 위 아래 오른쪽 왼쪽 앞 뒤 가 가능한지 체크

"""
import sys
from collections import deque as dq
input = sys.stdin.readline

def check(r, c, z, m, n, h):
    d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    p = []
    for dz, dr, dc in d:
        if 0 <= r + dr < n and 0 <= c + dc < m and 0 <= z + dz < h:
            p.append((z + dz, r + dr, c + dc))
    return p

def solution():
    m, n, h = map(int, input().split())

    days = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    tomatoes = []

    for _ in range(h):
        sub_tomatoes = []
        for _ in range(n):
            sub_tomatoes.append(list(map(int, input().split())))
        tomatoes.append(sub_tomatoes)

    q = dq([])
    max_day = 0
    for hh in range(h):
        for nn in range(n):
            for mm in range(m):
                if tomatoes[hh][nn][mm] == 1:
                    q.append((hh, nn, mm, 0))

    while q:
        z, r, c, day = q.popleft()

        d_list = check(r, c, z, m, n, h)
        if d_list == []:
            continue

        else:
            for dz, dr, dc in d_list:
                if tomatoes[dz][dr][dc] == 0:
                    days[dz][dr][dc] = day + 1
                    # min(days[dz][dr][dc], day + 1)
                    tomatoes[dz][dr][dc] = 1
                    q.append((dz, dr, dc, day + 1))

    for hh in range(h):
        for nn in range(n):
            if 0 in tomatoes[hh][nn]:
                return -1
            max_day = max(max_day, max(days[hh][nn]))
    print(tomatoes)
    print(days)
    return max_day

print(solution())