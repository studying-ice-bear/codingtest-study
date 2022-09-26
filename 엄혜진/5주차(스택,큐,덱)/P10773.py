import sys

input = sys.stdin.readline

# input = sys.stdin.readline
#
# k = int(input().rstrip())
# stack = []
# for _ in range(k):
#     n = int(input().rstrip())
#     if n == 0:
#         stack = stack[:-1]
#     else:
#         stack.append(n)
# # print(k, stack)
#
# print(sum(stack))
# 31620KB	4872ms


k = int(input().rstrip())
stack = []
for _ in range(k):
    n = int(input().rstrip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
# print(k, stack)

print(sum(stack))
# 31620KB	112ms