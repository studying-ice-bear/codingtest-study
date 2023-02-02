import sys
N, M, X = map(int, sys.stdin.readline().split())
village = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, t = map(int, sys.stdin.readline().split())
    village[x-1][y-1] = t
print(*village, sep='\n')

'''
curr = 0
visited = [False for _ in range(N)]
time = 0

while curr != X-1:
    print(village[curr])
    visited[curr] = True
    t = max(village[curr])
    curr = village[curr].index(t)
    time += t
    print("changed:", curr)

print(time)
'''
'''
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''