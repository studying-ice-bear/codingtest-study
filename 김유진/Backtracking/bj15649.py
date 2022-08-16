import sys, itertools
num, pick = map(int, sys.stdin.readline().split(" "))

permutation = itertools.permutations([i for i in range(1, num+1)], pick)
for p in permutation:
    for i in p:
        print(i, end=" ")
    print()