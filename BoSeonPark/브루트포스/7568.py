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
    
"""
풀이
리스트에 저장된 사람들에서 자시과 나머지 다른 사람을 비교해 자신보다 덩치가 큰 사람 수를 저장함
순서대로 자기보다 덩치가 큰 사람 수 + 1로 출력
"""