import sys

# 3월 1일 부터 11월 30일 끼지 매일 꽃 한가지 이상이 피어있어야 하는데 필요한 꽃의 개수

n = int(sys.stdin.readline().rstrip())
flower = [[] for _ in range(n)]
for i in range(n):
    b_m, b_d, f_m, f_d = map(int, sys.stdin.readline().split())
    flower[i] = [b_m * 100 + b_d, f_m * 100 + f_d]

# print(n, flower)

flower.sort(key=lambda x: (x[0], x[1]))
# print(flower)

answer = 0
current = 301
fall = 301

while flower:
    if fall >= 1201 or fall < flower[0][0]:
        break

    for _ in range(len(flower)):
        if flower[0][0] <= current:
            fall = max(fall, flower[0][1])
            flower.remove(flower[0])
        else:
            break
    answer += 1
    current = fall

print(0 if fall < 1201 else answer)
