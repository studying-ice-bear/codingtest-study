import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

s = 0
e = 0
tot = nums[s]
answer = 0

while s < n:   
    if e != n - 1:
        if tot < m:
            e += 1
            tot += nums[e]
        elif tot > m:
            tot -= nums[s]
            s += 1
        elif tot == m:
            answer += 1
            e += 1
            tot += nums[e]
    elif e == n - 1:
        if tot == m:
            answer += 1
        tot -= nums[s]
        s += 1
    
print(answer)