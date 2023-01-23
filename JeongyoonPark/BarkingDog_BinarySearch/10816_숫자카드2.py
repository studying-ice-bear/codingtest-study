from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
my_card = Counter(list(map(int,input().split())))
m = int(input())
card = list(map(int,input().split()))
result = []

for i in card:
    try:
        result.append(my_card[i])
    except:
        result.append(0)
print(*result)

# 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# my_card = list(map(int,input().split()))
# my_card.sort()
# m = int(input())
# card = list(map(int,input().split()))
# result = []

# for i in card:
#     try:
#         idx = my_card.index(i)
#         card2 = my_card[idx:]
#         result.append(card2.count(i))
#     except:
#         result.append(0)
# print(*result)