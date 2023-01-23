import sys

TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    clothes = {}
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        name, category = sys.stdin.readline().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    answer = 1
    for i in list(clothes.values()):
        answer *= (i + 1)

    print(answer - 1)
