import sys

N, D = map(int, sys.stdin.readline().split())

short = {}
for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if (start, end) in short.keys():
        short[(start, end)] = min(short[(start, end)], length)
    else:
        short[(start, end)] = length

print(short)

curr_s, curr_e = 0, 0
total = 0

for s, e in short.keys():
    print(s, e)
    if curr_s <= s:
        total += s-curr_s+short[(s, e)]
        # D = D-(e-s) + short[(s, e)]
        curr_s = s
        curr_e = e
    elif s < curr_e <= e:
        total -= s-curr_s+short[(s, e)]
        tmp = curr_e - curr_s - short[(curr_s, curr_e)]
        total += min(tmp, short[(s, e)])
    else:
        total += s - curr_s + short[(s, e)]

print(total)

'''
3 20
1 10 5 
2 10 1 
10 15 3


5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
{(0, 50): 10, (50, 100): 10, (100, 151): 10, (110, 140): 90}
10(0~50), 10(50~100), 70(남은 거리)

2 100
10 60 40 -> 60-10= 50, 40 -> 50-40 = 10
50 90 20 -> 90-50= 40, 20 -> 40-20 = 20
100 - 20 = 8 

'''
