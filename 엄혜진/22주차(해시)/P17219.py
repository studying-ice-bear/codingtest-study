import sys

n, m = map(int, sys.stdin.readline().split())
data = {}
for _ in range(n):
    url, pw = sys.stdin.readline().split()
    data[url] = pw

result = []
for _ in range(m):
    result.append(data[sys.stdin.readline().rstrip()])

print('\n'.join(result))
