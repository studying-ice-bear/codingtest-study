import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
for a in map(list, permutations(arr, M)):
    print(*a, sep=' ')
