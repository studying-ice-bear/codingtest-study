import sys
input = sys.stdin.readline

n = int(input())
timeTable = []
for i in range(n):
    s, e = map(int, input().split(' '))
    timeTable.append((s, e))

timeTable.sort(key = lambda x: (x[1], x[0]))

count = 1
a, b = timeTable[0][0], timeTable[0][1]

for s, e in timeTable[1:]:
    if s < b:
        continue
    else:
        count += 1
        a, b = s, e

print(count)