import sys
T = int(sys.stdin.readline())
M, N, K = map(int, sys.stdin.readline().split()) # 가로 길이, 세로 길이, 배추 위치 개수
garden = [[0] * M for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    garden[x][y] = 1
