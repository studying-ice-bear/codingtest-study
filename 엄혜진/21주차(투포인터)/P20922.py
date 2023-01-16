import sys
# n은 수열의 길이, k는 같은 원소를 몇 개까지 포함할 수 있는지
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# print(n, k, arr)

answer = 0

# 1. 시간초과 실패
# for start in range(n):
#     count = {}
#     cur_idx = 0
#     for end in range(start, n):
#         cur_idx = end
#         cur = arr[end]
#         if cur in count:
#             if count[cur] >= k:
#                 cur_idx -= 1
#                 break
#             else:
#                 count[cur] += 1
#         else:
#             count[cur] = 1
#     answer = max(answer, cur_idx - start + 1)
#     # print(start, count, answer)

# 2. 성공
left, right = 0, 0
count = [0] * (max(arr) + 1)

while right < n:
    if count[arr[right]] < k:
        count[arr[right]] += 1
        right += 1
    else:
        count[arr[left]] -= 1
        left += 1

    answer = max(answer, right - left)

print(answer)

