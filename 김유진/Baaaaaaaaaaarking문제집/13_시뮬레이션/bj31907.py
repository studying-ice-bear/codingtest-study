import sys
from collections import deque

N = int(sys.stdin.readline())  # 보드 크기: N * N
K = int(sys.stdin.readline())  # 사과의 개수

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 2

L = int(sys.stdin.readline())
change = {}
for _ in range(L):
    t, d = sys.stdin.readline().split()
    change[int(t)] = d

# snake = deque()
# snake.append((0, 0))
snake = deque([(0, 0)])

x, y = 0, 0
board[x][y] = 1
time = 0
direction = 0
def turn(a):
    global direction
    if a == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N:
        break

    if board[x][y] == 2:
        board[x][y] == 1
        snake.append((x, y))
        if time in change:
            turn(change[time])

    elif board[x][y] == 0:
        board[x][y] = 1
        snake.append((x, y))
        tx, ty = snake.popleft()
        board[tx][ty] = 0
        if time in change:
            turn(change[time])
    else:
        break

print(time)


'''
time = 0
# 북: 0, 동: 1, 남: 2, 서: 3
snake = {'head': [0, 0], 'tail': [0, 0], 'direction': 1}
i = 0


def turnDirection(dd):
    if change[i][1] == 'D':
        snake['direction'] = (snake['direction'] + 1) % 4
    else:
        snake['direction'] = snake['direction'] - 1 if (snake['direction'] - 1) > 0 else 3 - snake['direction']

def moveSnake():
    # 북: 0, 동: 1, 남: 2, 서: 3
    if snake['direction'] == 1:
        snake['head'][1] += 1
        snake['tail'][1] += 1
    elif snake['direction'] == 2:
        snake['head'][0] += 1
        snake['tail'][0] += 1
    elif snake['direction'] == 3:
        snake['head'][1] -= 1
        snake['tail'][1] -= 1
    else:
        snake['head'][0] -= 1
        snake['tail'][0] -= 1

def checkApple(cx, cy):
    if board[cx][cy] == 1:
        return True

while True:
    time += 1
    if change[i][0] == time:
        turnDirection(change[i][1])
        i += 1
    moveSnake()

    if board[snake['head'][0]][snake['head'][1]]:
        time += 1
        snake['tail'] = snake['head']

    if snake['head'][0] < 0 or snake['head'][0] >= N or \
            snake['head'][1] < 0 or snake['head'][1] >= N or \
            snake['tail'][0] < 0 or snake['tail'][0] >= N or \
            snake['tail'][1] < 0 or snake['tail'][1] >= N:
        break


print(time)
'''

'''
풀이 방법1.
while문을 활용해 시간을 계속 돌린다.

북: 0, 동: 1, 남: 2, 서: 3
북에서 왼쪽(L) : 0-1 => 3 서쪽 (0+3) // 4
동에서 왼쪽(L) : 1-1 => 0 북쪽 (1+3) // 4
남에서 왼쪽(L) : 2-1 => 1 동쪽
서에서 왼쪽(L) : 3-1 => 2 남쪽 

포인트:
'snake = {'head': [0, 0], 'tail': [0, 0], 'direction': 1}'
 snake를 객체 처리하는 것 -> board의 위치를 체크하는 것
 
코드 출처: https://hongcoding.tistory.com/127


'''
