import sys
input = sys.stdin.readline

n = int(input())

baseR, baseG, baseB = map(int, input().split(' '))
minR, minG, minB = 0, 0, 0

for i in range(1, n):
    r, g, b = map(int, input().split(' '))
    minR = r + min(baseG, baseB)
    minG = g + min(baseR, baseB)
    minB = b + min(baseR, baseG)
    
    baseR, baseG, baseB = minR, minG, minB

print(min(minR, minG, minB))
    