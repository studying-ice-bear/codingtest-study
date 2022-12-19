import sys
import itertools

n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

arr = list(itertools.product(num, repeat=m))
arr.sort()
for a in arr:
    print(' '.join(map(str, a)))
