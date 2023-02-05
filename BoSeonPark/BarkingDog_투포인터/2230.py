import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]
nums.sort()
answer = 2000000001
s, e = 0, 0


while s < n and e < n:
    r = nums[e] - nums[s]
    
    if r >= m:
        s += 1
        answer = min(answer, r)
    else:
        e += 1

print(answer)