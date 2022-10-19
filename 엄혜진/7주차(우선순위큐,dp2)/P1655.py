import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
# 1. 시간초과
# nums = []
# for _ in range(N):
#     x = int(input().rstrip())
#     nums.append(x)
#     nums.sort()
#     if len(nums) < 3:
#         print(nums[0])
#     else:
#         if len(nums) % 2 == 0:
#             print(nums[len(nums) // 2 - 1])
#         else:
#             print(nums[len(nums) // 2])

# 2. 40512KB	320ms
l = []
r = []
for i in range(N):
    x = int(input().rstrip())

    if i < 2:
        heapq.heappush(r, x)
    else:
        if x < r[0]:
            heapq.heappush(l, (-x, x))
        else:
            heapq.heappush(r, x)
        # print(l, r)

        if len(l) > len(r) - 1:
            heapq.heappush(r, heapq.heappop(l)[1])
        elif len(l) < len(r) - 2:
            temp = heapq.heappop(r)
            heapq.heappush(l, (-temp, temp))

    # print(l, r)
    print(r[0])



