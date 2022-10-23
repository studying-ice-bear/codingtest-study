"""
- 투 포인터

idea> 정렬 후 투포인터 사용하기
- arr의 원소는 서로 다른 자연수
- arr가 정렬되어 있다면, arr[i] + arr[j] = x 일 경우, arr[i+n] + arr[j-m] = x가 됨
- 시작점을 0, 끝점을 len(arr) - 1로 두고 조건에 맞게 범위 줄이기
"""
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

x = int(input())
arr.sort()
start = 0
end = len(arr) - 1
answer = 0
while start < end:
    if arr[start] + arr[end] > x:
        end -= 1
    else:
        if arr[start] + arr[end] == x:
            answer += 1
        start += 1

print(answer)
    