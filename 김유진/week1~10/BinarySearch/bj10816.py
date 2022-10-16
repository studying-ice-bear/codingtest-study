import sys
N = int(sys.stdin.readline())
sangun = list(map(int, sys.stdin.readline().split(" ")))

M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split(" ")))

sorted_sangun = sorted(sangun)
hash = {}
for san in sorted_sangun:
    if san not in hash.keys():
        hash[san] = 1
    else:
        hash[san] += 1

answer = []
for num in numbers:
    if num in hash.keys():
        answer.append(hash[num])
    else:
        answer.append(0)
print(*answer)

# answer = []
# for num in numbers:
#     check = 0
#     for s in sorted_sangun:
#         if num == s:
#             check += 1
#     answer.append(check)
#
# print(*answer)
