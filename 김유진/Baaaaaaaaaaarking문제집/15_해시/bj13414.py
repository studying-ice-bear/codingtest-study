import sys
K, L = map(int, sys.stdin.readline().split())

ready = {}
for i in range(L):
    input = sys.stdin.readline().strip()

    if input not in ready.keys():
        ready[input] = i+1
    else:
        ready[input] = i+1

for a, b in sorted(ready.items(), key=lambda item: item[1])[:K]:
    print(a)

'''
문제 링크: https://www.acmicpc.net/problem/13414
- 다른 풀이: reverse 사용
import sys
read = sys.stdin.readline
k, n = [int(i) for i in read().split()]
vals = [read().rstrip() for _ in range(n)]

vals.reverse()
vals = list(dict.fromkeys(vals))

k = min(k, len(vals))
print(*vals[:-k-1:-1])

'''
