import sys
from collections import deque

move = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    l = int(sys.stdin.readline().rstrip())
    current = list(map(int, sys.stdin.readline().rstrip().split()))
    goal = list(map(int, sys.stdin.readline().rstrip().split()))

    # print(l, current, goal)
    visited = [[0 for i in range(l)] for j in range(l)]


    def bfs(x, y, count):
        dq = deque()
        dq.append([x, y, count])
        visited[x][y] = 1
        while dq:
            x, y, cnt = dq.popleft()

            if x == goal[0] and y == goal[1]:
                print(cnt)
                break

            for m_x, m_y in move:
                new_x = x + m_x
                new_y = y + m_y
                if 0 <= new_x < l and 0 <= new_y < l and visited[new_x][new_y] == 0:
                    dq.append([new_x, new_y, cnt + 1])
                    visited[new_x][new_y] = 1


    bfs(current[0], current[1], 0)

# 32436KB	2080ms