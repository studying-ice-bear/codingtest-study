import sys, itertools
num, pick = map(int, sys.stdin.readline().split(" "))

combinations = itertools.combinations([i for i in range(1, num+1)], pick)
for c in combinations:
    for i in c:
        print(i, end=' ')
    print()
