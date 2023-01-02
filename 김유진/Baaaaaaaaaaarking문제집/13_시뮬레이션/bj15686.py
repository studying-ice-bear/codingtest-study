from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().split())
city = []
houses = []
chickens = []

for i in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

pickChicken = list(combinations(chickens, M))

cityChicken = []
for pick in pickChicken:
    minimumDistance = 0
    # print(pick)
    for house in houses:
        distances = []
        for chicken in pick:
            result = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            # print(house, chicken, result)
            distances.append(result)
        # print(min(distances))
        minimumDistance += min(distances)
    cityChicken.append(minimumDistance)
    # print(cityChicken)
print(min(cityChicken))

'''
문제 링크: https://www.acmicpc.net/problem/15686

치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리는 모든 집의 치킨 거리의 합

5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

houses = [[0,2], [1,4], [2,1], [3,2]]
chicken = [[1,2], [2,2], [4,4]]

'''