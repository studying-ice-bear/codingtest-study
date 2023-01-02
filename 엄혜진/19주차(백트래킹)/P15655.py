import sys
import itertools

n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
# print(n, m, num)

num.sort()
arr = list(itertools.combinations(num, m))
arr.sort()
for a in arr:
    print(' '.join(map(str, a)))
