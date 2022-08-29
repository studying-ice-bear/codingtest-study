import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

num_list = list(map(int, input().split(' ')))

prev = [sum(num_list[0:m])]

for i in range(m, n):
    prev.append(prev[i-m] - num_list[i-m] + num_list[i])
    
print(max(prev))