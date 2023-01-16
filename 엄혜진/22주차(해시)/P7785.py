import sys

n = int(sys.stdin.readline())
log = {}
for _ in range(n):
    p, s = sys.stdin.readline().split()
    if s == "enter":
        log[p] = s
    else:
        if p in log:
            del log[p]

print('\n'.join(reversed(sorted(log.keys()))))
