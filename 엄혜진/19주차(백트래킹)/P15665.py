import itertools
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

arr = sorted(set(list(itertools.product(num, repeat=m))))
for a in arr:
    print(' '.join(map(str, a)))
