import itertools
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

arr = set(list(itertools.permutations(num, m)))
for a in sorted(arr):
    print(' '.join(map(str, a)))
