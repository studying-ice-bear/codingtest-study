import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            target_x, target_y = i, j
            answer[i][j] = 0

visited = [[False for _ in range(j)] for _ in range(i)]

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([[x, y]])
    visited[x][y] = True

    while queue:
        now = queue.popleft()
        answer[now[0]][now[1]] = 0

        for xx in dx:
            for yy in dy:
                nx = x + xx
                ny = y + yy

                if 0 < nx < n and 0 < ny < m:
                    queue.push([nx, ny])
                    answer[nx][ny] = answer[x][y] + 1
                    visited[nx][ny] = True


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 or arr[i][j] == 0:
            answer[i][j] = 0
        else:
            answer[i][j] = bfs(i, j)
            # answer[i][j] = abs(target_x-i) + abs(target_y-j)

for ans in answer:
    print(*ans, sep=' ')


'''
문제링크: https://www.acmicpc.net/problem/14940

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
11 12 13 14 15 16 17 18 19 20 0(21) 0 0 0 25
12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
14 15 16 17 18 19 20 21 22 23 0 31 32 33 34


5 5
1 1 1 1 1
1 0 0 0 1
1 1 2 1 1
1 1 1 0 0
1 0 0 0 1

'''