import sys
input = sys.stdin.readline

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

for num in num_list:
    print(num)