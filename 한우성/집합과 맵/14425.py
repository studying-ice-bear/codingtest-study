import sys

n, m = map(int, sys.stdin.readline().split())
hash = set()
count = 0
for i in range(n):
    hash.add(sys.stdin.readline())
for check_str in range(m):
    check_str = sys.stdin.readline()
    if check_str in hash:
        count +=1

print(count)