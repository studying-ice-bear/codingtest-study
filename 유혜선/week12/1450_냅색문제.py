"""
- 투 포인터

idea> meet in the middle + 투 포인터
- meet in the middle 은 완전 탐색으로 하기엔 범위가 너무 클때,
탐색할 범위를 반으로 줄여서 계산하는 방법
=> 탐색할 arr를 반으로 쪼개기
- 이 문제는 최대 30개의 물건을 넣을지 말지 결정해야 하므로 2**30(약 10억)번의 연산 수행
- 물건을 반으로 나눠서 (15 + 15) 탐색하면 2**15(약 3만) * 2 => 6만번의 연산 수행

- 먼저 물건을 반으로 나눠(arr1, arr2) 물건을 포함하거나 안했을 경우 나올 수 있는 경우를 모두 구하고 (itertools 사용)
- 정렬 후
- arr1 또는 arr2를 기준으로 잡고 투포인터 탐색 수행
- sub_arr1의 원소와 sub_arr2의 원소를 더했을 때 기준 무게보다 같거나 적으면 
sub_arr2 원소의 위치 + 1(개수) 를 answer에 더해줌
- 크면 p2 -= 1
"""
import sys
from itertools import combinations as cb
input = sys.stdin.readline


# def combination(n):
#     arr = [[0] * (n + 1) for _ in range(n + 1)]
#     arr[1][0], arr[1][1] = 1, 1

#     for i in range(2, n+1):
#         arr[i][0] = 1
#         for j in range(1, n+1):
#             arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#     return arr

# cb = combination(30)

n, c = map(int, input().split())
arr = list(map(int, input().split()))

arr1 = arr[:(n//2)]
arr2 = arr[(n//2):]

# itertools의 combinations 를 이용해서 조합의 합 구하기
def sub_sum(arr, c):
    l = [0]
    for i in range(1, len(arr)+1):
        for t in list(cb(arr, i)):
            temp = sum(t)
            if temp <= c:
                l.append(temp)
    l.sort()
    return l

sub_arr1 = sub_sum(arr1, c)
sub_arr2 = sub_sum(arr2, c)

p1 = 0
p2 = len(sub_arr2) - 1

answer = 0

# 투포인터 활용 부분
for p1 in range(len(sub_arr1)):
    while 0 <= p2 < len(sub_arr2):
        if sub_arr1[p1] + sub_arr2[p2] <= c:
            answer += p2 + 1
            break
        else:
            p2 -= 1

print(answer) 
