import sys
N = int(sys.stdin.readline())
house = []
for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(3)]] * N
select = 0

dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1, N):
    house[i][0] = min(house[i - 1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]
    house[i][2] = min(house[i - 1][0], house[i - 1][1]) + house[i][2]

print(min(house[-1]))
'''
R - B - G
R - G - B
'''
