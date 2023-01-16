import sys
N, M = map(int, sys.stdin.readline().split())

findPassword = {}

for _ in range(N):
    web, pw = sys.stdin.readline().strip().split(' ')
    findPassword[web] = pw


for _ in range(M):
    print(findPassword[sys.stdin.readline().strip()])
