'''
문제 링크: https://www.acmicpc.net/problem/14503
문제 이해가 안되서 참고한 글: https://www.acmicpc.net/board/view/96605

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색을 진행한다.
    1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 체러 한 칸 후진을 하고 2번으로 돌아간다.
    4. 네 방향 모두 청소가 이미 되어 있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

N: 세로 크기, M: 가로 크기
(r, c) 방향 d
0: 북
1: 동
2: 남
3: 서

3 3
1 1 0
1 1 1
1 0 1
1 1 1
output:
1

5 4
1 1 0
1 1 1 1
1 0 0 1
1 0 0 1
1 0 1 0
1 0 0 0
output:
4

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
output:
57

0  0  0  0  0  0  0  0  0  0
 0 56 57 46 45 44 43 42 41  0
 0 55 48 47  0  0  0  0 40  0
 0 50 49  0  0 36 37 38 39  0
 0 51  0  0 35 34 31 30  0  0
 0 52 53 12 11 33 32 29 28  0
 0 54 14 13 10  9  0  0 27  0
 0 16 15  2  1  8  0  0 26  0
 0 17 18  3  4  7  0  0 25  0
 0 21 19 20  5  6 22 23 24  0
 0  0  0  0  0  0  0  0  0  0
'''

import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
place = []

for i in range(N):
    place.append(list(map(int, sys.stdin.readline().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
clean = 1
visited[r][c] = 1

while True:
    back = True
    for _ in range(4):
        d = (d+3) % 4
        x = r + directions[d][0]
        y = c + directions[d][1]

        if 0 <= x < N and 0 <= y < M and place[x][y] == 0:
            if visited[x][y] == 0:
                visited[x][y] = 1
                clean += 1
                r = x
                c = y
                back = False
                break

    if back:
        if place[r-directions[d][0]][c-directions[d][1]] == 1:
            print(clean)
            break
        else:
            r, c = r-directions[d][0], c-directions[d][1]


        # dd = (d + 2) // 4
        # dx = r + directions[dd][0]
        # dy = c + directions[dd][1]
        #
        # if 0 <= dx < N and 0 <= dy < M:
        #     r = dx
        #     c = dy
        #     if place[r][c] == 1:
        #         print(*place, sep='\n')
        #         break
        # else:
        #     print(*place, sep='\n')
        #     print(clean)
        #     break

'''
def getCheck(num):
    checkFromNorth = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    checkFromEast = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    checkFromSouth = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    checkFromWest = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    if num == 0:
        return checkFromNorth
    elif num == 1:
        return checkFromEast
    elif num == 2:
        return checkFromSouth
    elif num == 3:
        return checkFromWest


clean = 0
while True:
    directions = getCheck(d)

    if place[r][c] == 0:
        clean += 1
        place[r][c] = 2

    back = True
    for direction in directions:
        r = r + direction[0]
        c = c + direction[1]
        if 0 <= r < N and 0 <= c < M and place[r][c] == 0:
            d = 3 if d - 1 < 0 else d - 1
            back = False
            break

    if back:
        d = (d + 2) // 4  # 후진 방향
        r = r + directions[d][0]
        c = c + directions[d][1]
        if place[r][c] == 1:
            print(clean)
            break
'''

#
# while True:
#     place[r][c] = 1
#     clean += 1
#
#     print(r, c)
#     print(*place, sep='\n')
#
#     goback = False
#
#     check = getCheck(d)
#     print(d, "check: ", check)
#     for i in range(len(check)):
#         print(check[i])
#         x = r + check[i][0]
#         y = c + check[i][1]
#         if 0 <= x < N and 0 <= y < M and place[x][y] == 0:
#             print(x, y)
#             goback = False
#             r = x
#             c = y
#             d = i
#             break
#
#         goback = True
#
#     back = [[-1, 0], [0, -1], [1, 0], [0, -1]]
#     if goback:
#         dx = r + back[d][0]
#         dy = c + back[d][1]
#         if 0 <= dx < N and 0 <= dy < M and place[dx][dy] == 1:
#             break
#
# print(clean)


