from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    m = 51 * 2
    matrix = [[-1 for _ in range(m)] for _ in range(m)]

    # 도형 그리기
    for r in rectangle:
        lx, ly, rx, ry = map(lambda x: x * 2, r)
        for i in range(lx, rx + 1):
            for j in range(ly, ry + 1):
                if lx < i < rx and ly < j < ry:
                    matrix[i][j] = 0
                elif matrix[i][j] != 0:
                    matrix[i][j] = 1

    # 이동하기
    def bfs(s, e):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        dq = deque()
        s.append(0)
        dq.append(s)
        visited[s[0]][s[1]] = 1

        while dq:
            x, y, cnt = dq.popleft()

            for d in range(len(dx)):
                next_x = x + dx[d]
                next_y = y + dy[d]

                if not 0 < next_x < m or not 0 < next_y < m:
                    continue

                if matrix[next_x][next_y] == 1 and visited[next_x][next_y] == -1:
                    if next_x == e[0] and next_y == e[1]:
                        return (cnt + 1) // 2
                    dq.append([next_x, next_y, cnt + 1])
                    visited[next_x][next_y] = 1

    visited = [[-1 for _ in range(m)] for _ in range(m)]
    start = list(map(lambda x: x * 2, [characterX, characterY]))
    end = list(map(lambda x: x * 2, [itemX, itemY]))

    answer = bfs(start, end)
    # for p in range(30):
    #     print(visited[p][:30])
    return answer