import sys
from collections import deque
input = sys.stdin.readline

n  = int(input())
k = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    row, col = map(int, input().split())
    graph[row][col] = 1

l = int(input())
direction = deque([])

for i in range(l):
    x, c = input().split()
    direction.append((int(x), c))

print(direction)
# 현재 위치를 계속 추가하다가

# 시작 방향
# dx, dy = 0, 1
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
cur = 0

def game(x, y):
    global cur
    queue = deque([(x, y)])

    count = 0
    while True:
        count += 1

        x, y = queue[-1][0], queue[-1][1]
        nx, ny = x + dx[cur], y + dy[cur]
        # 머리 돌리는 조건
        if direction:
            if count == direction[0][0]:
                changeDirection(direction[0][1])
                direction.popleft()

        # 종료 조건
        if nx < 1 or nx > n or ny < 1 or ny > n:
            return count
        if (nx, ny) in queue:
            return count

        # 이동한 곳에 사과 있으면 다시 append
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            queue.append((nx, ny))
        else:
            queue.popleft()
            queue.append((nx, ny))


def changeDirection(dir):
    global cur
    if dir == 'L':
        cur = (cur - 1) % 4
    else:
        cur = (cur + 1) % 4

print(game(1, 1))


'''
from collections import deque

n  = int(input())
k = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    row, col = map(int, input().split())
    graph[row][col] = 1

graph[1][1] = 2
# print(graph)

l = int(input())
direction = []

for i in range(l):
    x, c = input().split()
    direction.append((int(x), c))
# print(direction)


# 현재 위치를 계속 추가하다가

# 시작 방향
# dx, dy = 0, 1
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
cur = 0

def game(x, y):
    global cur
    queue = deque([(x, y)])

    count = 0
    while True:
        count += 1

        # 머리 돌리는 조건
        # if count == direction[0][0]:
        #     if direction[0][1] == 'D':
        #         changeRight(dx, dy)
        #     else: changeLeft(dx, dy)
        #     direction.pop(0)
        if direction:
            print(count, direction[0][0])
            if count == direction[0][0]:
                changeDirection(direction[0][1])
                direction.pop(0)
        print(dx, dy)
        x, y = queue.pop()
        nx, ny = x + dx[cur], y + dy[cur]

        # 종료 조건
        if nx < 1 or nx > n or ny < 1 or ny > n:
            return count
        if graph[nx][ny] == 2:
            print(111111111)
            return count

        # 이동한 곳에 사과 있으면 다시 append
        if graph[nx][ny] == 1:
            graph[nx][ny] = 2
            queue.append((x, y))
            queue.append((nx, ny))
            graph[x][y] = 2
        else:
            queue.append((nx, ny))
            graph[x][y] = 0
            graph[nx][ny] = 2
        print(graph)


# def changeRight(dx, dy):
#     global dx, dy

#     if dx == 1: dx, dy = 0, -1
#     elif dy == -1: dx, dy = -1, 0
#     elif dx == -1: dx, dy = 0, 1
#     else: dx, dy = 1, 0

# def changeLeft(dx, dy):
#     if dx == 1: dx, dy = 0, 1
#     elif dy == -1: dx, dy = 1, 0
#     elif dx == -1: dx, dy = 0, -1
#     else: dx, dy = -1, 0


def changeDirection(dir):
    global cur
    if dir == 'L':
        cur = (cur - 1) % 4
    else:
        cur = (cur + 1) % 4

print(game(1, 1))
'''

