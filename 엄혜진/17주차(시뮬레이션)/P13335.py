import sys

# n개의 트럭(순서변경 불가, 무게 다양함)
# w 길이의 다리위해 w대의 트럭만 동시에 올라감
# 트럭들의 하중 <= L

# 1. 다리의 하중을 매번 더하여 계산한 경우: 32424KB	120ms
# 2. 현재 하중을 변수로 따로 관리한 경우: 32432KB	104ms

from collections import deque

n, w, L = map(int, sys.stdin.readline().rstrip().split())
truck = deque(list(map(int, sys.stdin.readline().rstrip().split())))

# print(n, w, L, truck)

# 1.
# time = 0
# bridge = deque([0] * w)
#
#
# while bridge:
#     # print(bridge)
#
#     # 다리를 다 지난 경우
#     bridge.popleft()
#
#     # 이제 다리에 들어온 경우
#     if truck:
#         if sum(bridge) + truck[0] <= L:
#             bridge.append(truck.popleft())
#         else:
#             bridge.append(0)
#
#     time += 1
#
# print(time)

# 2.
time = 0
bridge = deque([0] * w)
cur_w = 0

while bridge:
    # print(bridge)

    t = bridge.popleft()
    if t > 0:
        cur_w -= t

    if truck:
        if cur_w + truck[0] <= L:
            cur_w += truck[0]
            bridge.append(truck.popleft())
        else:
            bridge.append(0)

    time += 1

print(time)
