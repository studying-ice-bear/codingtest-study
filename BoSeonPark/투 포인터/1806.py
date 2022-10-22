import sys
input = sys.stdin.readline

n, s = map(int, input().split())
elements = list(map(int, input().split()))

l, r = 0, 0
answer = 100001

tot = elements[l]
t = 1

while True:
    if tot >= s and t < answer:
        answer = t
    
    if tot < s:
        r += 1
        if r == n:
            break
        t += 1
        tot += elements[r]
    elif tot >= s:
        tot -= elements[l]
        t -= 1
        l += 1

if answer == 100001:
    print(0)
else:
    print(answer)