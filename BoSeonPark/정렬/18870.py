import sys
input = sys.stdin.readline

n = int(input())
pos = list(map(int, input().split(' ')))

pos_dict = {val : i for i, val in enumerate(sorted(set(pos)))}

for p in pos:
    print(pos_dict[p], end=' ')
