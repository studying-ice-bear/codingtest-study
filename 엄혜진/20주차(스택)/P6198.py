import sys

n = int(sys.stdin.readline().rstrip())
h = []
answer = 0
for i in range(1, n + 1):
    cur = int(sys.stdin.readline().rstrip())
    if not h or h[-1] > cur:
        h.append(cur)
    else:
        while h and h[-1] <= cur:
            h.pop()
        h.append(cur)
    answer += len(h) - 1

print(answer)
