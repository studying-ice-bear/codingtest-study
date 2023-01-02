import sys
from collections import deque

# 64720KB	2296ms (147624KB	504ms)
# 불의 이동경로와 지훈의 이동경로를 같이 관리해야하는데, 불의 이동과 지훈의 이동을 덱큐에 모두 넣어서 하면 메모리 초과가 날거 같았다.
# 도저히 감이 안잡혀서 구글링을 했더니, 획기적인 방법 발견. 방문했다면 visited 시간을 저장하는 것이다.

# 불 방문시각과 지훈의 방문시각을 대소 비교만 했는데,
# 이 글을 읽고 https://ywtechit.tistory.com/76 대소 비교만 해서는 안된다는 것을 깨달았다.
# 방문하지 않은 경우가 -1이기 때문에 대소비교만 한다면, 방문하지 않은 곳임에도 불이 있다고 판단할 수 있기 때문이다.

r, c = map(int, sys.stdin.readline().rstrip().split())
matrix = []
current = []
f_current = []
for i in range(r):
    temp = sys.stdin.readline().rstrip()
    for j in range(len(temp)):
        if temp[j] == 'J':
            current = [i, j]
        if temp[j] == 'F':
            f_current.append((i, j))

    matrix.append(temp)


# print(matrix, current)

def bfs(start, graph):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    #  불의 이동 경로를 저장한다.
    f_dq = deque()
    f_visited = [[-1 for _ in range(c)] for _ in range(r)]
    for f_x, f_y in f_current:
        f_dq.append([f_x, f_y, 0])
        f_visited[f_x][f_y] = 0

    while f_dq:
        cur_f_x, cur_f_y, time = f_dq.popleft()

        for d_x, d_y in zip(dx, dy):
            move_x = cur_f_x + d_x
            move_y = cur_f_y + d_y

            if move_x < 0 or move_x >= r or move_y < 0 or move_y >= c or graph[move_x][move_y] == '#':
                continue

            if f_visited[move_x][move_y] == -1:
                f_visited[move_x][move_y] = time + 1
                f_dq.append([move_x, move_y, time + 1])

    # 지훈이의 이동 경로 저장한다.
    dq = deque()
    visited = [[-1 for _ in range(c)] for _ in range(r)]

    dq.append([start, 0])
    visited[start[0]][start[1]] = 0

    answer = 0
    while dq:
        cur, time = dq.popleft()

        for d_x, d_y in zip(dx, dy):
            move_x = cur[0] + d_x
            move_y = cur[1] + d_y

            if move_x < 0 or move_x >= r or move_y < 0 or move_y >= c:
                return time + 1

            if graph[move_x][move_y] == '#' or -1 < f_visited[move_x][
                move_y] <= time + 1:  # "불이 방문했고", 방문한 시각이 지훈이 방문한 시각보다 빠르면 안된다.
                continue

            if visited[move_x][move_y] == -1:
                visited[move_x][move_y] = time + 1
                dq.append([[move_x, move_y], time + 1])

    # for p in range(len(f_visited)):
    #     print(f_visited[p])
    # print()
    # for p in range(len(visited)):
    #     print(visited[p])

    return answer if answer > 0 else "IMPOSSIBLE"


print(bfs(current, matrix))
