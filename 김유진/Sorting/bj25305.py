import sys
N, k = map(int, sys.stdin.readline().split(' '))
arr = sorted(list(map(int, sys.stdin.readline().split(' '))), reverse=True)
print(arr[k-1])

'''
    다른 풀이
    Asterisk(*)
    Unpacking
    n, k, *l=map(int,open(0).read().split())
    print(sorted(l)[n-k])
'''