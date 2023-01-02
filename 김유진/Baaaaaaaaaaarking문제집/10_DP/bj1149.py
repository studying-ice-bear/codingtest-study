import sys
N = int(sys.stdin.readline())
house = []
for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    house[i][0] = min(house[i - 1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]
    house[i][2] = min(house[i - 1][0], house[i - 1][1]) + house[i][2]

print(min(house[-1]))

'''
문제 링크: https://www.acmicpc.net/problem/1149

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
2 <= i <= N-1

R - B - G
R - G - B

case1:
3
1 100 100
100 100 100
1 100 100

output:
102
'''
