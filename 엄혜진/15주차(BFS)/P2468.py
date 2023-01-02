import sys
from collections import deque

# 32476KB	1264ms

n = int(sys.stdin.readline().rstrip())
matrix = []
depth_max = 0
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    depth_max = max(depth_max, max(temp))
    matrix.append(temp)


# for m in range(n):
#     print(matrix[m])

def bfs(start, visited, rain):
    dq = deque()
    dq.append(start)
    visited[start[0]][start[1]] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while dq:
        x, y = dq.popleft()

        for d_x, d_y in zip(dx, dy):
            move_x = x + d_x
            move_y = y + d_y
            if move_x < 0 or move_x >= n or move_y < 0 or move_y >= n:
                continue
            if visited[move_x][move_y] == 0 and matrix[move_x][move_y] > rain:
                dq.append((move_x, move_y))
                visited[move_x][move_y] = 1


def count_land(rain):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for t in range(n):
        for k in range(n):
            if matrix[t][k] > rain and visited[t][k] == 0:
                bfs((t, k), visited, rain)
                cnt += 1
    # print(rain, cnt)
    # for m in range(n):
    #     print(visited[m])
    # print()
    return cnt


answer = 1 # 아무 지역도 안 잠기는 경우
for i in range(1, depth_max + 1):
    answer = max(answer, count_land(i))


print(answer)
