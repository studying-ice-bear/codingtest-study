import sys
input = sys.stdin.readline
n = int(input())
rope = sorted([int(input()) for i in range(n)])
weight = []

for i in range(n):
    weight.append(rope[i] * (n-i))
print(max(weight))