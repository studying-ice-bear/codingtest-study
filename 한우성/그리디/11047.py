import sys

a, amounts = map(int, sys.stdin.readline().split())

coins = []
count = 0

for i in range(a):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort(reverse=True)

for coin in coins:
    count += amounts//coin
    amounts = amounts % coin

print(count)