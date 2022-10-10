import sys

sys.setrecursionlimit(10 ** 9)

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())

    field = [[0 for i in range(M)] for j in range(N)]
    visited = [[0 for i in range(M)] for j in range(N)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        field[Y][X] = 1

    answer = 0


    # print(M, N, K, field)

    def dfs(E, x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return 0

        visited[x][y] = answer

        if 0 <= x - 1 < N and E[x - 1][y] == 1 and visited[x - 1][y] == 0:
            dfs(E, x - 1, y)
        if 0 <= y - 1 < M and E[x][y - 1] == 1 and visited[x][y - 1] == 0:
            dfs(E, x, y - 1)
        if 0 <= x + 1 < N and E[x + 1][y] == 1 and visited[x + 1][y] == 0:
            dfs(E, x + 1, y)
        if 0 <= y + 1 < M and E[x][y + 1] == 1 and visited[x][y + 1] == 0:
            dfs(E, x, y + 1)


    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0:
                answer += 1
                dfs(field, i, j)

    print(answer)

# 33220KB	84ms