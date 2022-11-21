import sys
from collections import deque

# pypy3 (220720KB	700ms) python3(시간초과)

# 1. 불이 번지는 시각 구하기
#  - 건물 안이어야 하고
#  - 벽이 아니어야 하고
#  - 먼저 번진 이력이 있으면 가장 빨리 도착한 불의 시각을 저장
# 2. 상근이가 도착하는 시각 구하기
#  - 건물 밖이면 탈출 성공이므로 도착한 시각을 임시 저장
#  - 벽이 아니어야 하고, 불이 번지는 시각보다 늦으면 안되고
#  - 도착한 이력이 있으면 가장 빨리 도착한 시각을 저장

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    matrix = []
    for i in range(h):
        matrix.append(sys.stdin.readline().rstrip())

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    f_visited = [[-1 for _ in range(w)] for _ in range(h)]
    man = []


    def f_bfs(f):
        f_dq = deque()

        for x, y in f:
            f_visited[x][y] = 0
            f_dq.append(([x, y], 0))

        while f_dq:
            cur, time = f_dq.popleft()
            for d in range(4):
                move_x = cur[0] + dx[d]
                move_y = cur[1] + dy[d]
                move_time = time + 1

                if move_x < 0 or move_x >= h or move_y < 0 or move_y >= w:
                    continue
                elif matrix[move_x][move_y] == '#':
                    continue
                elif f_visited[move_x][move_y] == -1 or move_time < f_visited[move_x][move_y]:
                    f_dq.append(([move_x, move_y], move_time))
                    f_visited[move_x][move_y] = move_time

    fire = []
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '*':
                fire.append([i, j])
            elif matrix[i][j] == '@':
                man = [i, j]

    f_bfs(fire)

    def bfs(start):
        dq = deque()
        visited = [[-1 for _ in range(w)] for _ in range(h)]

        dq.append((start, 0))
        visited[start[0]][start[1]] = 0

        answer = 0

        while dq:
            cur, time = dq.popleft()

            for d in range(4):
                move_x = cur[0] + dx[d]
                move_y = cur[1] + dy[d]
                move_time = time + 1

                if move_x < 0 or move_x >= h or move_y < 0 or move_y >= w:
                    answer = move_time if answer == 0 else min(move_time, answer)
                elif matrix[move_x][move_y] == '#' or -1 < f_visited[move_x][move_y] <= move_time:
                    continue
                elif visited[move_x][move_y] == -1 or move_time < visited[move_x][move_y]:
                    dq.append(([move_x, move_y], move_time))
                    visited[move_x][move_y] = move_time

        return answer if answer > 0 else "IMPOSSIBLE"


    print(bfs(man))

