# 여기서는 좌표 1부터 시작
# 반복을 돌면서 1에서 bfs해서 2를 발견하면 그 거리 구하고 -> 응. 이거 아니야

from sys import stdin
from itertools import combinations

input = stdin.readline
n, m = map(int, input().split())
# 전체 graph를 받아올 필요가 없음.
# graph = [list(map(int,input().split())) for _ in range(n)]

# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, -> 아? 경우의 수?

house, chicken = [], []
for i in range(n):
    graph = list(map(int,input().split()))
    for j in range(n):
        if graph[j] == 1:
            house.append((i+1,j+1))
        elif graph[j] == 2:
            chicken.append((i+1,j+1))

# print(house)
# print(chicken)

def distance(a,b):
    distance = abs(a[0]-b[0]) + abs(a[1]-b[1])
    return distance

# float("inf")
min_distance = 100000
# sum_distance = 0

for chi in combinations(chicken, m):
    sum_distance = 0
    for hou in house:
# 않이...여기서... 또 완전탐색..? 이거 맞아?
        sum_distance += min([distance(hou, i) for i in chi])
    # min_distance = min(min_distance, sum_distance)
    # 새로 구한 거리 합이 더 작으면 min 값을 업데이트
    if sum_distance < min_distance:
            min_distance = sum_distance
    # sum_distance = 0

print(min_distance)

# 엥 이게 시간 초과가 안나?