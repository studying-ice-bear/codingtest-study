import itertools
import sys

test = list(map(int, sys.stdin.readline().split()))
while test[0] > 0:
    k = test[0]
    s = test[1:]

    arr = list(itertools.combinations(s, 6))
    for a in arr:
        print(' '.join(map(str, a)))
    print()

    test = list(map(int, sys.stdin.readline().split()))
