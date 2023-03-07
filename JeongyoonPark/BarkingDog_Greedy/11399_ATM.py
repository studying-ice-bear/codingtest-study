import sys
input = sys.stdin.readline
n = int(input())
p = sorted(list(map(int,input().split())))
sum = 0
for i in range(n):
    sum += p[i] * (n-i)
print(sum)