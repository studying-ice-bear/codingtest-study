"""
- 투 포인터

idea> 정렬 후 투포인터 사용하기
- liquid의 원소 범위는 -1,000,000,000 ~ 1,000,000,000
- 시작점을 0, 끝점을 len(arr) - 1로 두고 두 원소 합의 **절댓값** 을 줄이도록 범위 지정
- liquid[start] + liquid[end]가 0보다 크면 end -= 1 로 절댓값을 줄이고
- liquid[start] + liquid[end]가 0보다 작으면 start += 1 로 절댓값을 줄인다.
"""
import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

start = 0
end = n-1

min_compound = abs(liquid[0] + liquid[n-1])
answer = (liquid[start], liquid[end])

while start < end:
    compound = liquid[start] + liquid[end]
    if compound == 0:
        answer = (liquid[start], liquid[end])
        break

    if min_compound > abs(compound):
        answer = (liquid[start], liquid[end])
        min_compound = abs(compound)

    if compound > 0:
        end -= 1
    else:
        start += 1


print(*answer, sep=" ")
