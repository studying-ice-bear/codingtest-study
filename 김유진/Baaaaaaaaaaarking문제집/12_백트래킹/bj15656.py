import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for a in map(list, product(arr, repeat = M)):
    print(*a, sep=' ')
