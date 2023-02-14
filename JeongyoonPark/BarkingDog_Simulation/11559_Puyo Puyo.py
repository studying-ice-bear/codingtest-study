from collections import deque
import sys
input = sys.stdin.readline

# 1) bfs 돌려서 4번 이상 가면 (같은 색) 1연쇄가 시작.
# 2) 연쇄 후 아래로 떨어지게 된다.

def bfs(i, j):
    global flag
    queue = deque()
    queue.append([i, j])

    pang = [[i, j]]
    visited[i][j] = True
    # cnt = 1
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and game_map[nx][ny] == game_map[i][j] and not visited[nx][ny]:
                visited[nx][ny] = True
                # cnt += 1
                pang.append([nx,ny])
                queue.append([nx,ny])
    # 쓰읍.. 무조건 같을 때 'pang'으로 바꿔줬더니 4개 이상 아닐 때 다시 되돌리기 힘드네..?
    # 그러면 4이상 됐을 때 바꿔줘야하는데 어떻게 할까
    # cnt로 개수를 세지말고 값을 넣어두고 그거의 len을 비교?
    # if cnt >= 4:
    # return cnt
    if len(pang) >= 4:
        flag = True
        for i, j in pang:
            game_map[i][j] = '.'


# 뿌요는 위에서 아래로 떨어짐 (중력)
# def drop_puyos():
#     for i in range(12):
#         for j in range(6):
#             if game_map[i][j] != '.' and i != 11:
#                 if game_map[i+1][j] == '.':
#                     game_map[i+1][j] = game_map[i][j]
#                     game_map[i][j] = '.'

# def drop_puyos():
#     # 11번 째는 떨어질 곳이 없으니깐 10부터 시작
#     for i in range(10,-1,-1):
#         for j in range(6):
#             if game_map[i][j] != '.':
#                 if game_map[i+1][j] == '.':
#                     game_map[i+1][j] = game_map[i][j]
#                     game_map[i][j] = '.'


def drop_puyos():
    # 세로 방향으로 생각해서 6줄 중에서
    for i in range(6):
        # 밑에서부터아래로 떨어뜨릴 뿌요 검색
        # 근데 가장 바닥에 있는 뿌요는 확인안해도 되기 때문에
        for j in range(10, -1, -1):
            # 밑에서 부터 뿌요가 있는 곳까지
            # game_map[j][i] != "." 뿌요가 있는 위치가 '.'이 아닌
            for k in range(11, j, -1):
                if game_map[j][i] != "." and game_map[k][i] == ".":
                    game_map[k][i] = game_map[j][i]
                    game_map[j][i] = "."
                    break

game_map = [list(input().strip()) for i in range(12)]
dx, dy = (0,1,0,-1), (1,0,-1,0)
cnt = 0

# bfs() 하고 drop() 반복하다가 멈춰야함
while True:
    flag = False
    visited = [[False]*6 for _ in range(12)]    

    for i in range(12):
        for j in range(6):
            if game_map[i][j] != '.' and not visited[i][j]:
                bfs(i,j)
    
    # 다 돌았는데 아직도 bfs 결과가 False면 끝~
    if not flag: 
        break
    drop_puyos()
    cnt += 1


print(cnt)