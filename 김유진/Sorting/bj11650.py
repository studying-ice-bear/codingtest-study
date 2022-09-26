import sys

N = int(sys.stdin.readline())
dot = []
x_dot = []
y_dot = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dot.append([x, y])

for d in sorted(dot):
    print(d[0], d[1])