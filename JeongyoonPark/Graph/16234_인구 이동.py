import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0,1,0,-1), (1,0,-1,0)

'''
경계 확인해서 범위에 맞으면 queue에 넣음. queue에 있는 나라는 연합.
'''

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    total = population[x][y]
    country = [(x,y)]

    while queue:
        x, y = queue.popleft()
        current = population[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                difference =  abs(current - population[nx][ny])
                if l <= difference <= r:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    country.append((nx,ny))
                    total += population[nx][ny]
    
    if len(country) > 1:
        new_population = total // len(country)
        for xx, yy in country:
            population[xx][yy] = new_population
        return True
    return False


flag = True
count = 0
while flag:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j): 
                    flag = True
    if flag: count += 1
                

print(count)