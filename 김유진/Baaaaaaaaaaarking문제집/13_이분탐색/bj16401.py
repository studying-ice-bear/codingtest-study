import sys

N, M = map(int, sys.stdin.readline().split())
snack = list(map(int, sys.stdin.readline().split()))


def bs(arr, n):
    left, right = 1, max(snack)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = 0

        if mid == 0:
            return 0

        for a in arr:
            cnt += a // mid

        if cnt >= n:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result


print(bs(snack, N))

'''
★문제 링크: https://www.acmicpc.net/problem/16401
문제 풀이 아이디어: https://velog.io/@kmh9250/%EB%B0%B1%EC%A4%8016401-%EA%B3%BC%EC%9E%90-%EB%82%98%EB%88%A0%EC%A3%BC%EA%B8%B0
=> 과자의 길이에 대한 데이터를 이분탐색하는 방법
- 과자의 길이 중 가장 긴 값을 right, 가장 작은 값, 즉 1을 left로 설정
- 이 left, right 값의 mid 값을 각 배열에 나눈다.
- 나눈 몫은 나눠줄 수 있는 조카들의 수! cnt 값!
- 이 값을 M(조카의 수)과 비교
    - cnt가 M보다 큰 경우
        left값 갱신
        mid+1?
    - cnt가 M보다 작은 경우
        right값 갱신
        mid-1? mid? mid-1!
    * 범위가 1e6이니까 빠르게 갱신하기 위해서 mid값을 기준으로 잡기

4 3
10 10 15
7
'''
