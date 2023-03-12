import sys
N = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().split()))
money = int(sys.stdin.readline())

left, right = 0, max(request)


while left <= right:
    mid = (left + right) // 2

    total = 0
    for r in request:
        if r <= mid:
            total += r
        else:
            total += mid

    if total < money:
        right += 1
    else:
        left += 1

print(mid)

'''
4
120 110 140 150
485
'''