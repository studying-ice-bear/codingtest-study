import sys, copy

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def left(graph):
    for i in range(N):
        top = 0
        for j in range(1, N):
            if graph[i][j]:
                tmp = graph[i][j]
                graph[i][j] = 0

                if graph[i][top] == 0:
                    graph[i][top] = tmp
                elif graph[i][top] == tmp:
                    graph[i][top] = tmp * 2
                    top += 1
                else:
                    top += 1
                    graph[i][top] = tmp

    return graph

def right(graph):
    for i in range(N):
            top = N-1
            for j in range(N-2, -1, -1):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0

                    if graph[i][top] == 0:
                        graph[i][top] = tmp
                    elif graph[i][top] == tmp:
                        graph[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        graph[i][top] = tmp
    return graph

def up(graph):
    for j in range(N):
        top = 0
        for i in range(1, N):
            if graph[i][j]:
                tmp = graph[i][j]
                graph[i][j] = 0
                if graph[top][j] == 0:
                    graph[top][j] = tmp
                elif graph[top][j] == tmp:
                    graph[top][j] = tmp * 2
                    top += 1
                else:
                    top += 1
                    graph[top][j] = tmp
    return graph

def down(graph):
    for j in range(N):
        top = N - 1
        for i in range(N - 2, -1, -1):
            if graph[i][j]:
                tmp = graph[i][j]
                graph[i][j] = 0

                if graph[top][j] == 0:
                    graph[top][j] = tmp
                elif graph[top][j] == tmp:
                    graph[top][j] = tmp * 2
                    top -= 1
                else:
                    top -= 1
                    graph[top][j] = tmp
    return graph

def move(graph, dir):
    if dir == 0:
        for i in range(N):
            top = N-1
            for j in range(N-2, -1, -1):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0

                    if graph[i][top] == 0:
                        graph[i][top] = tmp
                    elif graph[i][top] == tmp:
                        graph[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        graph[i][top] = tmp

    elif dir == 1:
        for i in range(N):
            top = 0
            for j in range(1, N):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0

                    if graph[i][top] == 0:
                        graph[i][top] = tmp
                    elif graph[i][top] == tmp:
                        graph[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        graph[i][top] = tmp
    elif dir == 2:  # up
        for j in range(N):
            top = 0
            for i in range(1, N):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0
                    if graph[top][j] == 0:
                        graph[top][j] = tmp
                    elif graph[top][j] == tmp:
                        graph[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        graph[top][j] = tmp
    else:
        for j in range(N):
            top = N-1
            for i in range(N-2, -1, -1):
                if graph[i][j]:
                    tmp = graph[i][j]
                    graph[i][j] = 0

                    if graph[top][j] == 0:
                        graph[top][j] = tmp
                    elif graph[top][j] == tmp:
                        graph[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        graph[top][j] = tmp

    return graph

def dfs(graph, cnt):
    global answer
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, graph[i][j])
        return

    # deepcopy 주의!
    dfs(left(copy.deepcopy(graph)), cnt+1)
    dfs(right(copy.deepcopy(graph)), cnt + 1)
    dfs(up(copy.deepcopy(graph)), cnt + 1)
    dfs(down(copy.deepcopy(graph)), cnt + 1)

    # for i in range(4):
    #     tmp_graph = move(copy.deepcopy(graph), i)
    #     dfs(tmp_graph, cnt+1)

answer = 0
dfs(graph, 0)
print(answer)

'''
3
2 0 2
0 4 4
0 0 2
'''
# 좌로 이동
# 투 포인터
# 3
# 0 0 2
# 2 2 0
# 4 4 0
# for i in range(N):
#     left, right = N - 2, N - 1
#
#     while 0 <= left < N and 0 <= right < N:
#         if graph[i][left] != 0:
#             if graph[i][right] != 0:
#                 graph[i][right] = graph[i][left] * 2
#             else:
#                 graph[i][right] = graph[i][left]
#
#             graph[i][left] = 0
#             right = left
#             left = right - 1
#         else:
#             left -= 1
# print(*graph, sep='\n')

# 우로 이동

    # 하드코딩 방법 X
    # print(i)
    # at = 0
    # cnt = 0
    #
    # for j in range(N):
    #     if graph[i][j]:
    #
    #         at = j
    #         cnt += 1
    #
    # print(at, j)
    #
    # if cnt == 1:
    #     graph[i][N-1] = graph[i][at]
    #     graph[i][at] = 0
    # else:
    #     graph[i][at] = graph[i][j] * 2
    #     graph[i][j] = 0
    #
    # print(*graph, sep='\n')


'''
4
0 0 2 0
0 0 0 0
2 0 0 0
0 0 0 0

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 
이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. 
(실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)


3
2 2 2
4 4 4
8 8 8

3
0 2 4
0 4 8
0 8 16


3
2 4 0
4 8 0
8 16 0

--------
2 0 2
0 0 0
4 0 4

'''