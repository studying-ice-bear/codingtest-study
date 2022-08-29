import sys
input = sys.stdin.readline

n = int(input())
timeTalbe = list(map(int, input().split(' ')))

timeTalbe.sort()
total = 0
a = 0
for t in timeTalbe:
    a += t
    total += a

print(total)
    