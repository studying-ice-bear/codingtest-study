import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

num_list = list(map(int, input().split(' ')))

prev = [0]
temp = 0
for num in num_list:
    temp += num
    prev.append(temp)

for _ in range(m):
    i, j = map(int, input().split(' '))
    print(prev[j] - prev[i-1])
    