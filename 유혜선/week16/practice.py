import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    matrix = []
    fire = []
    man = []

    for i in range(h):
        matrix.append(list(sys.stdin.readline().rstrip()))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    f_dq = deque()
    f_visited = [[-1 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "@":
                man = [i, j]

            if matrix[i][j] == "*":
                f_dq.append((i, j, 0))
                f_visited[i][j] = 0

                while f_dq:
                    x, y, time = f_dq.popleft()
                    for d in range(4):
                        move_x = x + dx[d]
                        move_y = y + dy[d]

                        if move_x < 0 or move_x >= h or move_y < 0 or move_y >= w:
                            continue
                        if matrix[move_x][move_y] != '#' and f_visited[move_x][move_y] == -1:
                            f_dq.append((move_x, move_y, time + 1))
                            f_visited[move_x][move_y] = time + 1
    print(f_visited)
    dq = deque()
    visited = [[-1 for _ in range(w)] for _ in range(h)]

    dq.append((man, 0))
    visited[man[0]][man[1]] = 0

    answer = 0

    while dq:
        if answer > 0:
            break

        cur, time = dq.popleft()

        for d in range(4):
            move_x = cur[0] + dx[d]
            move_y = cur[1] + dy[d]

            if move_x < 0 or move_x >= h or move_y < 0 or move_y >= w:
                answer = time + 1
                continue
            if matrix[move_x][move_y] == '#' or -1 < f_visited[move_x][move_y] <= time + 1:
                continue
            if visited[move_x][move_y] == -1:
                dq.append(([move_x, move_y], time + 1))
                visited[move_x][move_y] = time + 1

    print(f"답{_}: ", answer if answer > 0 else "IMPOSSIBLE")

