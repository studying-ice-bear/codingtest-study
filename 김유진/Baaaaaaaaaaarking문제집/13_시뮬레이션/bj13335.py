import sys

# n은 다리를 건너는 트럭의 수, w는 다리의 길이, L은 다리의 최대하중
n, w, L = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))

bridge = [0] * w

weight = 0
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
print(time)

# bridge = [0] * w
# que = []
# time = 0
# total = 0
# count = 0
#
# for truck in trucks:
#     if total+truck < L:
#         total += truck
#         count += 1
#     else:
#
#         time += w + count
#
#         total = 0
#         count = 0


# for truck in trucks:
#     if sum(que) < L:
#         que.append(truck)
#         if sum(que) < L:
#             print(que)
#     else:
#         if len(que) < w:
#             time += len(que) + w
#         else:
#             time += w*(len(que)//w)
#
#         que = []
#
#         print(time)
#
# print(time)

'''
문제 링크: https://www.acmicpc.net/problem/13335

1. 트럭의 합 < 최대 하중
    queue에 넣어주고,
2. queue의 길이가 < w -> n+w?
    queue의 길이가 w보다 크면 -> w*(queue길이//w)?

- 다리에 건너는 중 -> queue의 개수만큼 == w(다리의 길이)
- 다리를 완전히 다 건너는 경우에 다음 트럭을 보낼 수 있다. -> w


4 2 10
7 4 5 6
output:
8

3 3 3
1 1 1
output:
6

3 4 3
1 1 1
output:
7
'''