'''
처음 아기상어 크기 : 2
이동 : 자신 크기보다 작거나 같거나
먹음 : 자신보다 작음
성장 : 자기의 크기와 같은 수의 물고기를 먹으면 성장
    먹고 나면 그 자리는 0이 된다.(빈칸)
    크기가 2일 때 물고기 두 마리 먹으면 3이 된다.
'''
from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

dx, dy = (0,-1,0,1), (1,0,-1,0)

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            cur_x, cur_y = i, j

# 가까운 먹이를 찾는 탐색 -> `BFS`
# BFS를 사용할 시 입력: 현재 아기 상어의 위치
# 출력: 후보를 리스트

def bfs(cur_x,cur_y):
    visited = [[0] * n for _ in range(n)]
    queue = deque([(cur_x,cur_y)])
    temporary = []

    visited[cur_x][cur_y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if space[cur_x][cur_y] > space[nx][ny] > 0:
                    visited[nx][ny] = visited[x][y] + 1
                    temporary.append((visited[nx][ny] - 1, nx, ny))
                elif space[cur_x][cur_y] == space[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                elif space[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return sorted(temporary, key = lambda x: (x[0], x[1], x[2]))

time = 0
size = [2,0]
while True:
    space[cur_x][cur_y] = size[0]
    temporary = deque(bfs(cur_x, cur_y))

    if not temporary: break

    step, nx, ny = temporary.popleft()
    time += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    
    space[cur_x][cur_y] = 0
    cur_x, cur_y = nx, ny

print(time)

'''
from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9: 
            queue = deque([(i,j)])
            break

# 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기
dx, dy = (0,-1,0,1), (1,0,-1,0)

print(space)

def sum_check():
    result = 0
    for i in space:
        result += sum(i) 
    return result == 9

# queue에 아기상어 현재 위치
def bfs():
    temp = 0
    current_size = 2
    time = 0 

    while queue:
        x, y = queue.popleft()
        space[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and space[nx][ny] <= current_size:
                time += 1
                temp += 1
                if current_size != space[nx][ny]: space[nx][ny] = 0
                queue.append((nx,ny))
                break
        
        if temp == current_size:
            current_size += 1
    return time

print(bfs())
'''


