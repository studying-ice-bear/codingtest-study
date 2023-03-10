import sys
H, W = map(int, sys.stdin.readline().split())
rain = list(map(int, sys.stdin.readline().split()))
buildings = [[0 for _ in range(W)] for _ in range(H)]

for i, r in zip(range(W), rain):
    for j in range(r):
        buildings[j][i] = 1

answer = 0

for i in range(H):
    l, r = 0, 1
    while l <= r and r < W:
        if buildings[i][l] and buildings[i][r]:
            answer += r - l - 1
            l = r
            r += 1
        elif buildings[i][l] and not buildings[i][r]:
            r += 1
        elif not buildings[i][l] and buildings[i][r]:
            l = r
            r += 1
        else:
            l += 1
            r += 1

print(answer)

'''
4 4
3 0 1 4

[1, 0, 1, 1]
[1, 0, 0, 1]
[1, 0, 0, 1]
[0, 0, 0, 1]

4 8
3 1 2 3 4 1 1 2
[1, 1, 1, 1, 1, 1, 1, 1]
[1, 0, 1, 1, 1, 0, 0, 1]
[1, 0, 0, 1, 1, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
'''