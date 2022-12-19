import itertools
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

num.sort()

arr = sorted(set(list(itertools.combinations_with_replacement(num, m))))
for a in arr:
    print(' '.join(map(str, a)))
