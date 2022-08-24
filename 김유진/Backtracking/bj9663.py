'''
    N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
'''
import sys
N = int(sys.stdin.readline())

def left(m, cnt):
    if m-1 < 0:
        return cnt
    return left(m-1, cnt+1)

def right(m, cnt):
    if m+1 >= N:
        return cnt
    return right(m+1, cnt+1)

def up(n, cnt):
    if n-1 < 0:
        return cnt
    return up(n-1, cnt+1)

def down(n, cnt):
    if n+1 >=N:
        return cnt
    return down(n+1, cnt+1)

def diagonal_upleft(n, m, cnt):
    if n-1 < 0 or m-1 < 0:
        return cnt
    cnt += 1
    return diagonal_upleft(n-1, m-1, cnt)

def diagonal_upright(n, m, cnt):
    if n-1 < 0 or m+1 >= N:
        return cnt
    cnt += 1
    return diagonal_upright(n-1, m+1, cnt)

def diagonal_downleft(n, m, cnt):
    if n+1 >= N or m-1 < 0:
        return cnt
    cnt += 1
    return diagonal_downleft(n+1, m-1, cnt)

def diagonal_downright(n, m, cnt):
    if n+1 >= N or m+1 >= N:
        return cnt
    cnt += 1
    return diagonal_downright(n+1, m+1, cnt)


arr = [[0 for i in range(N)] for j in range(N)]
# arr = [0 for i in range(N)]
print(arr)

'''
[0, 2, 3, 1]
1행 2열
2행 3열
3행 1열
'''
count = 0
result = 0
for i in range(N):
    for j in range(N):
        count = 0
        count = up(i, count)
        count = down(i, count)
        count = left(j, count)
        count = right(j, count)
#         count += 2 * (N - 1)
        count = diagonal_upright(i, j, count)
        count = diagonal_upleft(i, j, count)
        count = diagonal_downleft(i, j, count)
        count = diagonal_downright(i, j, count)
        print(i, j ,count)
        result += N*N-1-count
        print(N*N-1-count)

print(result)
# print((N*N-1)*(N*N))
# print(count)
# print((N*N-1)*(N*N)-count)
