from re import S
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split(' ')))
s = [num_list[0]]

for i in range(1, n):
    s.append(max(num_list[i], s[i-1]+num_list[i]))

print(max(s))