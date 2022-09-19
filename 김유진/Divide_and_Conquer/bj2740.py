import sys

N, M = map(int, sys.stdin.readline().split())
matrix1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
N2, M2 = map(int, sys.stdin.readline().split())
matrix2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N2)]

result = [[0 for _ in range(M2)] for _ in range(N)]
for i in range(N):
    for j in range(M2):
        for k in range(M):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
        print(result[i][j], end=' ')
    print()
'''
2 2
1 0
0 1
2 3
1 1 1 
1 1 1
'''

'''
import sys
In = sys.stdin.readline
Out = sys.stdout.write

def main():
    n, m = map(int, In().split())
    a = [[*map(int, In().split())] for _ in range(n)]
    In()
    b = [[*map(int, In().split())] for _ in range(m)]
    ab = [[sum(x*y for x, y in zip(r, c)) for c in zip(*b)] for r in a]
    for row in ab:
        Out(' '.join(map(str, row)) + '\n')

main()
'''