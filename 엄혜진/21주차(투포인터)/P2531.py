import sys
from collections import deque

# 모든 경우의 수는 구하기 쉽지만, 서로다른 종류의 초밥을 먹는 경우를 구하는 게 어려워보인다.

# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int, sys.stdin.readline().split())

# 시도 3: 변수로 투포인터 만들어서 접근
# python3은 실패 pypy3은 성공
belt = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# print(n, d, k, c, belt)

answer = 0
start, end = 0, 0

while start < n:
    interval_arr = set()
    coupon_is_usable = True
    for cur_idx in range(start, start + k):
        cur_idx %= n
        interval_arr.add(belt[cur_idx])
        if belt[cur_idx] == c:
            coupon_is_usable = False

    cur_cnt = len(interval_arr)
    if coupon_is_usable:
        cur_cnt += 1
    answer = max(answer, cur_cnt)
    # print(interval_arr, start)

    start += 1

print(answer)

# 시도 2: 배열을 인덱스로 접근, 부분배열들을 배열로 저장하지 않고 set으로 저장해서 시간 절약하자, 쿠폰으로 먹을 수 있는지 여부를 플래그 변수로 두자
# python3은 실패 pypy3은 성공
# belt = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# # print(n, d, k, c, belt)
#
# answer = 0
#
# for start in range(n):
#     interval_arr = set()
#     coupon_is_usable = True
#     for end in range(start, start + k):
#         cur_idx = end % n
#         interval_arr.add(belt[cur_idx])
#         if belt[cur_idx] == c:
#             coupon_is_usable = False
#
#     cur_cnt = len(interval_arr)
#     if coupon_is_usable:
#         cur_cnt += 1
#     answer = max(answer, cur_cnt)
#     # print(interval_arr, start)
# print(answer)

# 시도 1: 덱의 rotate로 하려고 했으나 시간초과로 실패
# belt = deque([int(sys.stdin.readline().rstrip()) for _ in range(n)])
# # print(n, d, k, c, belt)
#
# answer = 0
#
# for start in range(n):
#     end = 0
#     interval_arr = []  # 먹은 초밥
#     while len(interval_arr) < k and end < n:
#         interval_arr.append(belt[end])
#         end += 1
#
#     # print(start, interval_arr)
#     if c not in interval_arr:
#         interval_arr.append(c)
#     answer = max(answer, len(set(interval_arr)))
#
#     belt.rotate(-1)
#
# print(answer)
