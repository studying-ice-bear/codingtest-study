import sys, itertools
num, pick = map(int, sys.stdin.readline().split(" "))

combinations = itertools.combinations([i for i in range(1, num+1)], pick)
for c in combinations:
    for i in c:
        print(i, end=' ')
    print()

'''
def back_tracking():
    if len(stack) == M:
        print(' '.join(list(map(str, stack))))
    else:
        for num in range(1, N + 1):
            if num not in stack:
                stack.append(num)
                back_tracking()
                stack.pop()


N, M = map(int, input().split())
stack = []
back_tracking()
'''
