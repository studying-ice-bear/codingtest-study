import sys
input = sys.stdin.readline

def checking(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            if temp[i+sy][j+sx] + sticker[sy][sx] > 1:
                return False
    return True

def attach(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            temp[i+sy][j+sx] += sticker[sy][sx]
    return

def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])

    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result


Y, X, k = map(int, input().split())
notebook = [[0] * X for _ in range(Y)]

for _ in range(k):
    y, x = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(y)]
    chk = False
    cnt = 0
    while cnt < 4:
        if chk == True:
            break
        for i in range(Y - len(sticker) + 1):
            if chk == True:
                break
            for j in range(X - len(sticker[0]) + 1):
                if checking(notebook, sticker):
                    attach(notebook, sticker)
                    chk = True
                    break
        sticker = rotate_90(sticker)
        cnt += 1

answer = 0
for i in range(Y):
    for j in range(X):
        answer += notebook[i][j]

print(answer)

# import sys
# N, M, K = map(int, sys.stdin.readline().split())
# nb = [[0 for i in range(M)] for j in range(N)]
#
# def fit(copy, arr, row, column):
#     while True:
#         check = True
#         for i in range(row):
#             for j in range(column):
#                 c = arr[i][j]
#                 if c == 0:
#                     continue
#                 elif c == 1 and copy[r][i] == 0:
#                     copy[i][j] = 1
#                 elif c == 1 and copy[r][i] == 1:
#                     check = False
#                     break
#
#         if check:
#             return nb
#             break
#         else:
#             # 90도 회전
#             new_arr = [[0 for i in range(row)] for j in range(column)]
#             for i in range(row):
#                 for j in range(column):
#                     if arr[i][j] == 1:
#                         nr = j
#                         nc = c-i
#                         new_arr[nr][nc] = arr[i][j]
#             arr = new_arr
#
# for k in range(K):
#     R, C = map(int, sys.stdin.readline().split())
#     s = []
#
#     for r in range(R):
#         ss = list(map(int, sys.stdin.readline().split()))
#         s.append(ss)
#
#     new_nb = fit(nb, s, R, C)



'''
문제 링크: https://www.acmicpc.net/problem/18808
1. 스티커를 회전시키지 않고 모눈종이에서 떼어낸다.
2. 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서 스티커를 붙일 수 있는 위치를 찾는다. 
    혜윤이는 노트북의 위쪽부터 스티커를 채워 나가려고 해서, 스티커를 붙일 수 있는 위치가 여러 곳 있다면 가장 위쪽의 위치를 선택한다. 
    가장 위쪽에 해당하는 위치도 여러 곳이 있다면 그중에서 가장 왼쪽의 위치를 선택한다.
3. 선택한 위치에 스티커를 붙인다. 
    만약 스티커를 붙일 수 있는 위치가 전혀 없어서 스티커를 붙이지 못했다면, 스티커를 시계 방향으로 90도 회전한 뒤 2번 과정을 반복한다.
4. 위의 과정을 네 번 반복해서 스티커를 0도, 90도, 180도, 270도 회전시켜 봤음에도 스티커를 붙이지 못했다면 해당 스티커를 붙이지 않고 버린다.

 0, 0, 0, 0
 0, 0, 0, 0
 0, 0, 0, 0
 0, 0, 0, 0
 0, 0, 0, 0
 
 1, 0, 1, 0
 1, 1, 1, 0
 1, 0, 1, 0
 0, 0, 0, 0
 0, 0, 0, 0
'''