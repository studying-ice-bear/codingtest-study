import sys
input = sys.stdin.readline
n = int(input())
result = 0

plus_arr = []
minus_arr = []
zero_count = 0

for _ in range(n):
    i = int(input())
    if i < 0: minus_arr.append(i)
    elif i == 0: zero_count += 1
    elif i > 1: plus_arr.append(i)
    elif i == 1: result += i

# O(N Log N)
plus_arr.sort(reverse=True)
minus_arr.sort()

temp = []
for p in plus_arr:
    if len(temp) == 1: 
        result += temp[0] * p
        temp = []
        continue
    temp.append(p)   

if len(temp) == 1: result += temp[0]
elif len(temp) == 2: result += temp[0] * temp[1]

temp2 = []
for m in minus_arr:
    if len(temp2) == 1: 
        result += temp2[0] * m
        temp2 = []
        continue
    temp2.append(m)   

if len(temp2) == 1: 
    if zero_count == 0: result += temp2[0]
elif len(temp2) == 2: result += temp2[0] * temp2[1]

print(result)

'''
경우 파악
1. 1은 무조건 더해주는게 더 큰 경우
2. 음수는 짝수 개는 각각 곱해서 더하고 홀수 개는 마지막 1개가 0이 있을 땐 사라지고 0이 없으면 더해줌.
'''

'''
# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])
'''