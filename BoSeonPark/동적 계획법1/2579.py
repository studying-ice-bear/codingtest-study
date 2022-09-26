import sys
input = sys.stdin.readline

n = int(input())
    
a = [0]*300
b = [0]*300

b[0] = int(input())

if n == 1:
    print(b[0])
    exit()

a[1] = int(input())
b[1] = a[1] + b[0]

if n == 2:
    print(b[1])
    exit()

for i in range(2, n):
    temp = int(input())
    a[i] = max(a[i-2], b[i-2]) + temp
    b[i] = a[i-1] + temp

print(max(a[n-1], b[n-1]))


"""
풀이
num 10 20 15 25 10 20
a   10 20 25 55 45 75 
b   10 30 35 50 65 65

a 이전걸 포함안한 합계 max(a[i-2], b[i-2]) + num[i]
b 이전걸 포함한 합계 a[i-1] + num[i]
"""