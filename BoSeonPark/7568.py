import sys
f = sys.stdin.readline

n = int(f())
peoples = []
for _ in range(n):
    x, y = map(int, f().split())
    peoples.append([x, y, 0])
    
for i in range(n):
    for j in range(n):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            peoples[i][2] += 1

for p in peoples:
    print(p[2]+1, end=' ')