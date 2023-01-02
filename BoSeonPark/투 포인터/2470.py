import sys
input = sys.stdin.readline

n = int(input())
acid = list(map(int, input().split()))
acid.sort()
l, r = 0, n-1
a, b, c = 0, 0, 2e+9+1

while l != r:
    temp = acid[l] + acid[r]
    if abs(temp) < c:
        a, b, c = acid[l], acid[r], abs(temp)
    
    if temp < 0:
        l += 1
    else:
        r -= 1

print(a, b)