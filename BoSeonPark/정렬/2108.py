import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort()
num_dict = Counter(num_list).most_common(2)
print(round(sum(num_list)/n))
print(num_list[n // 2])
if n == 1:
    print(num_list[0])
else:
    if num_dict[0][1] == num_dict[1][1]:
        print(num_dict[1][0])
    else:
        print(num_dict[0][0])
print(num_list[-1] - num_list[0])