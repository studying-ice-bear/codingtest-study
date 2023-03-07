import sys

N, M = map(int, sys.stdin.readline().split())
arr = [i for i in range(0, 9)]

isused = [False] * N

def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ');
        print()
        return

    for i in range(N):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            func(k+1)
            isused[i] = False

func(0)

'''
import sys
from itertools import permutations
arr.sort()
for a in map(list, permutations(arr, M)):
    print(*a, sep=' ')
'''