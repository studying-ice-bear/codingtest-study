import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
for a in map(list, combinations(arr, M)):
    print(*a, sep=' ')
