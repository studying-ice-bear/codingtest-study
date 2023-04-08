from collections import deque

M, S = map(int, input().split())
sea = [[[] for _ in range(5)] for _ in range(5)]

m = []

# 물고기 위치
for _ in range(M):
    i, j, k = map(int, input().split())
    if k == -2 or k == -1:
        continue
    sea[i][j].append(k)
    m.append((i, j))

# 상어 위치
x, y = map(int, input().split())

fishMoves = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
sharkMoves = [[], [-1, 0], [0, -1], [1, 0], [0, 1]]


def fishMove(moves):
    fishSmell = []
    tmp = sea.copy()

    for m_x, m_y in moves:
        for d in sea[m_x][m_y]:
            nx = m_x + fishMoves[d][0]
            ny = m_y + fishMoves[d][1]

            direction = tmp[m_x][m_y].pop()
            try_directions = [False for _ in range(9)]
            try_directions[0] = True
            new_d = direction

            while True:
                if try_directions[new_d]:
                    tmp[m_x][m_y].append(direction)
                    break

                try_directions[new_d] = True

                if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                    new_d = new_d-1 if new_d-1 > 0 else 8
                    nx = m_x + fishMoves[new_d][0]
                    ny = m_y + fishMoves[new_d][1]

                elif -1 in sea[nx][ny] or -2 in sea[nx][ny]:
                    new_d = new_d - 1 if new_d - 1 > 0 else 8
                    nx = m_x + fishMoves[new_d][0]
                    ny = m_y + fishMoves[new_d][1]
                    if (nx, ny) not in fishSmell:
                        fishSmell.append((nx, ny))
                    continue

                elif 0 < nx <= 4 and 0 < ny <= 4:
                    tmp[nx][ny].append(new_d)
                    break

    for smell in fishSmell:
        s_x, s_y = smell
        n = tmp[s_x][s_y].pop()
        n += 1
        if n == 0:
            tmp[s_x][s_y].pop()
        else:
            tmp[s_x][s_y].append(n)

    return tmp


def sharkmove(x, y, cnt):
    global shark
    if cnt == 3:
        return

    for i in range(0, 5):
        nx = x + sharkMoves[i][0]
        ny = y + sharkMoves[i][1]

        if 0 < nx <= 4 and 0 < ny < 4 and not visited[nx][ny]:
            visited[nx][ny] = True
            sharkMoves(nx, ny, cnt+1)
            visited[nx][ny] = False


# m = [[4, 3], [1, 3], [2, 4], [2, 1], [3, 4]]
# m = [[2, 1]]

for _ in range(S):
    sea = fishMove(m)
    visited = [[False] * 5 for _ in range(5)]

    shark = []

    sharkMoves(x, y, 0)



'''
9 1
4 3 5
1 3 5
2 4 2
1 1 -2
1 2 -2
3 1 -2
3 2 -2
2 1 6
3 4 4
4 2


M = 4
S = 1

sea[1][1].append(-2)
sea[1][2].append(-2)
sea[2][2].append(-2)
sea[3][1].append(-2)
sea[3][2].append(-2)

sea[4][3].append(5)
sea[1][3].append(5)
sea[2][4].append(2)
sea[2][1].append(6)
sea[3][4].append(4)
'''
