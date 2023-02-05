import sys

m, n = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# print(m, n, arr)

answer = 0
left, right = 1, max(arr)
while left <= right:
    # 중앙값
    mid = (left + right) // 2
    # 과자의 길이가 중앙값인 경우 몇 명에게 과자를 나눠줄 수 있는가?
    cnt = 0
    for i in range(n):
        cnt += arr[i] // mid
    # 모두에게 나눠주지 못하면 과자의 길이를 줄이고, 모두에게 나누어 줄 수 있다면 과자 길이를 늘인다.
    if cnt >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)

# 같은 코드인데 python3은 4272ms가 걸리고, pypy3는 836ms이 걸린다.
# 반복되는 연산이 많아서 pypy3가 더 빠르게 처리되는 거 같다.
