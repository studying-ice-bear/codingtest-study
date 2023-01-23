import sys

n, p, q = map(int, sys.stdin.readline().split())
a = {}
a[0] = 1

def A(i):
    if i in a:
        return a[i]

    a[i] = A(i // p) + A(i // q)

    return a[i]

print(A(n))