import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

total = 0
for i in range(len(coins) - 1, -1, -1):
    # print(coins[i])
    if k == 0:
        break

    if k >= coins[i]:
        temp = k // coins[i]
        # print('temp', temp, coins[i])
        k -= coins[i] * temp
        total += temp
        # print(total)

sys.stdout.write(str(total))

# 30840KB	68ms

