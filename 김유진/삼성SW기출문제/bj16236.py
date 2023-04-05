from collections import deque
N = int(input())

sea = []

for _ in range(N):
    sea.append(list(map(int, input().split(' '))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
def dfs(q, to_x, to_y, total, visited):

    while q:
        x, y = q.popleft()
        if to_x == x and to_y == y:
            return total
        total += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(q, nx, ny, total, visited)



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
                que.append((i, j, sea[i][j]))
                go[i][j] = True
            elif sea[i][j] == 0:
                go[i][j] = True

    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if not que:
        break

    x, y = start
    # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    if len(que) == 1:
        a, b, c = que.pop()
        time += abs(x-a) + abs(y-b)

        start = (a, b)
        sea[a][b] = 9

        eaten += 1

    else:
        # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
        # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
        canEat = 400
        x, y = start
        to = start

        for i in range(len(que)):
            a, b, c = que[i]
            total = abs(x-a) + abs(y-b)

            # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
            if total < canEat:
                canEat = total
                to = (a, b, c)
            # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
            elif total == canEat:
                if to[0] > a:
                    to = (a, b, c)
                elif to[0] == a:
                    if to[1] > b:
                        to = (a, b, c)
        
        
        sea[x][y] = 0
        sea[to[0]][to[1]] = 9

        time += canEat
        eaten += 1
        '''
        total = dfs(que, start[0], start[1], 0, go)
        print(total)
        time += total
        '''
    if eaten == babyshark:
        babyshark += 1
        eaten = 0

print(time)

'''
3
0 0 0
0 0 0
0 9 0

[size, time]

[2, 3] [2, 2] [2, 3]
[2, 2] [2, 1] [2, 2]
[2, 1] [2, 0] [2, 1]

'''
