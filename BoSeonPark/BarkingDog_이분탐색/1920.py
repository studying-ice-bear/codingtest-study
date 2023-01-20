import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    s, e = 0, n - 1
    flag = False
    while s <= e:
        m = (e + s) // 2
        
        if num == a[m]:
            flag = True
            break
        elif num > a[m]:
            s = m + 1
        elif num < a[m]:
            e = m - 1
    
    if flag:
        print(1)
    else:
        print(0)