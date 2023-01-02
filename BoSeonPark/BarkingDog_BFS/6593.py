import sys
from collections import deque
input = sys.stdin.readline

def bfs(b, v, k, i, j, l, r, c):
    # 북 동 남 서 상 하
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    df = [0, 0, 0, 0, 1, -1]
    
    v[k][i][j] = 1
    
    queue = deque([[k, i, j]])
    while queue:
        f, x, y = queue.popleft()
        
        for i in range(6):
            nf = f + df[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nf < l and 0 <= nx < r and 0 <= ny < c and v[nf][nx][ny] == 0:
                if b[nf][nx][ny] == '.':
                    v[nf][nx][ny] = v[f][x][y] + 1
                    queue.append([nf, nx, ny])
                elif b[nf][nx][ny] == 'E':
                    print('Escaped in %d minute(s).'%(v[f][x][y]))
                    return
    
    print('Trapped!')


f, x, y = 0, 0, 0
ef, ex, ey = 0, 0, 0 
while True:
    l, r, c = map(int, input().split())
    
    if l == 0 and r == 0 and c == 0:
        break
    
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    building = []
    
    for k in range(l):
        temp = []
        for i in range(r):
            temp.append(list(input().strip()))
            for j in range(c):
                if temp[i][j] == 'S':
                    f, x, y = k, i, j
                elif temp[i][j] == 'E':
                    ef, ex, ey = k, i, j
        input()
        building.append(temp)
    
    bfs(building, visited, f, x, y, l, r, c)