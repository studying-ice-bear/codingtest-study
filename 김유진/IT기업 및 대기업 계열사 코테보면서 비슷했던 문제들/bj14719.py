import sys
H, W = map(int, sys.stdin.readline().split())
building = list(map(int, sys.stdin.readline().split()))
building = building[::-1]
print(building)

rain = 0
tall = building[0]

for i in range(1, W):
    if building[i] < tall:
        rain += tall - building[i]
    else:
        tall = 0

print(rain)

# rain = 0
# tall = 0
# stack = []
# arr = []
#
# tall = building[0]
# for i in range(1, W):
#     if building[i] < tall:
#         arr.append(tall-building[i])
#         rain += tall - building[i]
#     else:
#         tall = max(tall, building[i])
#
# for i in range(W):
#     if not stack:
#         stack.append(building[i])
#     else:
#         if stack[-1] > building[i]:
#             stack.append(building[i])
#         elif max(stack) == building[i]:
#             for h in stack:
#                 rain += max(stack) - h
#             stack = []
#
# print(rain)

'''
for i in range(W-1):
    if building[i] > building[i+1]:
        rain[i] = building[i] - building[i+1]
        tall = max(tall, building[i])
    else:
        if tall > building[i+1]:
            rain[i] = tall - building[i+1]
        else:
            tall = max(tall, building[i+1])
'''