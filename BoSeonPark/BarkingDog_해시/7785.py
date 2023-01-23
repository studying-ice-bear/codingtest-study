import sys
input = sys.stdin.readline

n = int(input())

record = dict()

for _ in range(n):
    name, c = input().strip().split()
    
    if c == 'leave':
        del record[name]
    else:
        record[name] = c

temp = list(record.keys())
temp.sort(reverse=True)

for name in temp:
    print(name)