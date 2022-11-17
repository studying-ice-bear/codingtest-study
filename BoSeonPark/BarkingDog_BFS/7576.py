# 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

temp = []
box = []

for i in range(n):
    box.append(list(map(int, input().split())))
    
    for j in range(m):
        if box[i][j] == 1:
            temp.append([i, j])

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
while len(temp) != 0:
    tomato = deque(temp)
    temp = []
    answer += 1
    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    temp.append([nx, ny])

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()

print(answer-1)