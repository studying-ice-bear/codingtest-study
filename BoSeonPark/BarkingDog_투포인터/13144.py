import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
v = [False for _ in range(n + 1)]
answer = 0

e = 0

for s in range(n):
    while e < n:
        if v[nums[e]]:
            break
        
        v[nums[e]] = True
        e += 1
        
    answer += e - s
    v[nums[s]] = False
    
print(answer)
