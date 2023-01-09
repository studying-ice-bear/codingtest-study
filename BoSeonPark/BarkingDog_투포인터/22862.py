import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))
even = 0
answer = 0
cnt = 0
e = 0

for s in range(n):
    while cnt <= k and e < n:
        if nums[e] % 2 != 0:
            cnt += 1
        else:
            even += 1
        e += 1
            
        if s == 0 and e == n:
            answer = even
            break
    
    if cnt == k + 1:
        answer = max(answer, even)
    
    if nums[s] % 2 == 1:
        cnt -=1
    else:
        even -=1

print(answer)
