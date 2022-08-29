import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
count = 0
coin_list = []
for i in range(n):
    coin = int(input())
    if coin <= k:
        coin_list.append(coin)
        

while k != 0:
    if coin_list[-1] > k:
        coin_list.pop()
    else:
        count += k // coin_list[-1]
        k = k % coin_list[-1]

print(count)