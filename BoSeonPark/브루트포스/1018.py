import sys
f = sys.stdin.readline

n, m = map(int, f().split(' '))

count = []
board = []

for _ in range(n):
    board.append(f())
    
for r in range(n-7):
    for c in range(m-7):
        count1 = 0
        count2 = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        count1 += 1
                    if board[i][j] != 'B':
                        count2 += 1
                else:
                    if board[i][j] != 'B':
                        count1 += 1
                    if board[i][j] != 'W':
                        count2 += 1
        count.append(min(count1, count2))

print(min(count))
