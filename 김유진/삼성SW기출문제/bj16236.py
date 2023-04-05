from collections import deque

N = int(input())

sea = []

for _ in range(N):
    sea.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def countMove(graph, abletoMove, startpoint):
    moveGraph = [[0] * N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    a, b = startpoint
    que = deque()
    que.append((a, b))
    visited[a][b] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and abletoMove[nx][ny] and not visited[nx][ny]:
                moveGraph[nx][ny] = moveGraph[x][y] + 1
                que.append((nx, ny))
                visited[nx][ny] = True

    return moveGraph


babyshark = 2
eaten = 0
time = 0

while True:
    que = deque()
    go = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
            if sea[i][j] == 9:
                start = (i, j)
                sea[i][j] = 0
                go[i][j] = True
            elif sea[i][j] != 0 and sea[i][j] < babyshark:
                que.append((i, j))
                go[i][j] = True
            elif sea[i][j] == 0 or sea[i][j] <= babyshark:
                go[i][j] = True

    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if not que:
        break

    moveGraph = countMove(sea, go, start)
    x, y = start

    # print(time)
    # print("shark: ", babyshark, eaten)
    # print(x, y)
    # print(*sea, sep='\n')
    # print()
    # print(*moveGraph, sep='\n')
    # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    if len(que) == 1:
        a, b = que.pop()
        time += moveGraph[a][b]

        start = (a, b)
        sea[a][b] = 9

        eaten += 1

    else:
        # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
        # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
        canEat = 402
        to = start

        while que:
            qx, qy = que.popleft()
            distance = moveGraph[qx][qy]

            if distance == 0:
                to = start
            else:
                if canEat > distance:
                    canEat = distance
                    to = (qx, qy)

                elif canEat == distance:
                    if to[0] > qx:
                        to = (qx, qy)
                    elif to[0] == qx:
                        if to[1] > qy:
                            to = (qx, qy)


        time += moveGraph[to[0]][to[1]]
        sea[to[0]][to[1]] = 9
        eaten += 1

        if to == start:
            break

    if eaten == babyshark:
        babyshark += 1
        eaten = 0

print(time)

'''
5
0 0 5 0 0
0 6 1 7 0
8 2 0 3 10
0 9 4 11 0
0 0 12 0 0

3
0 1 1
4 4 4
0 9 0

5
1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 3
0 0 0 3 9

5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
9 2 3 4 5
1 2 3 4 5

10
9 2 0 0 0 0 0 0 0 1 
0 3 0 0 0 0 0 0 0 0
3 3 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

20
9 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0



3
0 0 0
0 0 0
0 9 0

[size, time]

[2, 3] [2, 2] [2, 3]
[2, 2] [2, 1] [2, 2]
[2, 1] [2, 0] [2, 1]

----------------------------
agraph =[
    [4, 3, 2, 1],
    [0, 0, 0, 0],
    [0, 0, 9, 0],
    [1, 2, 3, 4]
]

aMove = [
    [False, False, False, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, False, False, False]
]

N = 4

start = (2, 2)
------------------------------------

# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
def dfs(x, y, visited, a, b, total):
    visited[x][y] = True

    if x == a and y == b:
        return total

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            total = dfs(nx, ny, visited, a, b, total+1)
            visited[nx][ny] = False

'''
