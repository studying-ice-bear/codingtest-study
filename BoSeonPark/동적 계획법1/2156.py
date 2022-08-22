import sys
input = sys.stdin.readline

n = int(input())

a = [0] * n
b = [0] * n
c = [0] * n

a[0] = int(input())
b[0] = a[0]
c[0] = a[0]

if n == 1:
    print(a[0])
    exit()

a[1] = int(input())
b[1] = a[0] + a[1]
c[1] = a[0]

if n == 2:
    print(b[1])
    exit()

for i in range(2, n):
    temp = int(input())
    a[i] = c[i-1] + temp
    b[i] = a[i-1] + temp
    c[i] = max(a[i-1], b[i-1], c[i-1])

print(max(a[n-1], b[n-1], c[n-1]))


"""
06 10 13 09 08 01
06 10 19 25 31 29
06 16 23 28 33 32
06 06 16 23 28 33

00 00 10 00 05 10 00 00 01 10
00 00 10 00 15 20 15 25 26 35
00 00 10 10 05 25 20 15 26 36
00 00 00 10 10 15 25 25 25 26

이전거 포함 X = c[i-1] + num[i]
이전거 포함 O = a[i-1] + num[i]
자기자신 제외 = max(a[i-1], b[i-1], c[i-1])
"""