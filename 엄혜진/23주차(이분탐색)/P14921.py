import sys

n = int(sys.stdin.readline().rstrip())
liquid = list(map(int, sys.stdin.readline().split()))
# print(n, liquid)

left, right = 0, n - 1
answer = liquid[left] + liquid[right]

while left < right:
    # print(left, right)
    temp = liquid[left] + liquid[right]
    if abs(answer) > abs(temp):
        answer = temp

    if temp < 0:
        left += 1
    else:
        right -= 1

print(answer)
