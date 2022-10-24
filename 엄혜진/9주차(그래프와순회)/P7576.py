import sys
from collections import deque

# 1.
# affect = [[-1, 0], [0, -1], [1, 0], [0, 1]]
#
# M, N = map(int, sys.stdin.readline().rstrip().split())
# box = []
# riped = []
# unripe = 0
# visited = [[0 for i in range(M)] for j in range(N)]
# for i in range(N):
#     row = list(map(int, sys.stdin.readline().rstrip().split()))
#     for j in range(len(row)):
#         if row[j] == 1:
#             riped.append([i, j])
#
#         elif row[j] == -1:
#             visited[i][j] = -1
#         elif row[j] == 0:
#             unripe += 1
#     box.append(row)
#
#
# # print(M, N, box)
#
#
# def bfs(Vs, day):
#     global unripe
#
#     dq = deque()
#
#     for x, y in Vs:
#         dq.append([x, y, day])
#         visited[i][j] = 1
#
#     while dq:
#         print(dq)
#         x, y, d = dq.popleft()
#
#         if unripe == 0:
#             print(visited, unripe)
#             return d
#             break
#
#         for a_x, a_y in affect:
#             new_x = x + a_x
#             new_y = y + a_y
#             if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y] == 0:
#                 dq.append([new_x, new_y, d + 1])
#                 visited[new_x][new_y] == 1 # 나 뭐하냐... == 뭐임...
#                 unripe -= 1
#     return d
#
#
# if len(riped) == M * N:
#     print(0)
# elif len(riped) == 0:
#     print(-1)
# else:
#     print(bfs(riped, 0))

# 2. 161432KB	2164ms
# 길을 잃었따... 어딜 가야하나..
# 블로그 참고해서 다시 작성해본다

affect = [[-1, 0], [0, -1], [1, 0], [0, 1]]

M, N = map(int, sys.stdin.readline().rstrip().split())
box = []
riped = []
visited = []
answer = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(row)):
        if row[j] == 1:
            riped.append([i, j])
    box.append(row)
    visited.append(row)


# print(box, riped)

def bfs(Vs):
    dq = deque()
    for v_x, v_y in Vs:
        dq.append([v_x, v_y])

    while dq:
        # for k in range(len(box)):
        #     print(box[k])
        # print()
        x, y = dq.popleft()
        for a_x, a_y in affect:
            new_x = x + a_x
            new_y = y + a_y
            # print(new_x, new_y)
            if 0 <= new_x < N and 0 <= new_y < M and box[new_x][new_y] == 0:
                dq.append([new_x, new_y])
                visited[new_x][new_y] = visited[x][y] + 1


bfs(riped)
# print(visited)

for i in range(len(visited)):
    for j in range(len(visited[0])):
        if visited[i][j] == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(visited[i]))
print(answer - 1)

# 1번 방법이 틀린게 아니라 ==을 쓰는 바람에 코드가 안 돌아간 것이다..
# 컴퓨터가 아니라 내가 문제가 있는 것이거늘...