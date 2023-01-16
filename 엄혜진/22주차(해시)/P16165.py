import sys

N, M = map(int, sys.stdin.readline().split())
group = {}
member = {}
for _ in range(N):
    g = sys.stdin.readline().rstrip()
    personnel = int(sys.stdin.readline().rstrip())

    temp = []
    for _ in range(personnel):
        m = sys.stdin.readline().rstrip()
        temp.append(m)
        member[m] = g
    group[g] = sorted(temp)

for _ in range(M):
    name = sys.stdin.readline().rstrip()
    kind = int(sys.stdin.readline().rstrip())
    if kind == 0:
        print('\n'.join(group[name]))
    else:
        print(member[name])
