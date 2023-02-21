import sys

N, K = map(int, sys.stdin.readline().split())

durability = list(map(int, sys.stdin.readline().split()))

belt = zip([i for i in range(2*N)], durability)
move = [[x, y, False] for x, y in zip([i for i in range(2*N)], durability)]
# [위치, 내구도, 로봇 유무]
def checkZero():
    for i in range(N):
        if move[i][1] == 0:
            return True
    return False

cnt = 0
while True:
    # 올리는 위치
    for i in range(N):
        at = move[i][0]
        dur = move[i][1]
        robot = move[i][2]
        if not robot:
            robot = True
            dur -= 1
            if dur == 0:
                cnt += 1

            for j in range(i, N):
                if not move[j][2]:
                    robot = False
                    move[j][2] = True
                    move[j][1] -= 1
                    robot = move[j][2]


    # 내리는 위치
    for i in range(N, 2*N):
        move[i][2] = False

    if checkZero():
        break


'''
3 2
1 2 1 2 1 2

    1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
'''