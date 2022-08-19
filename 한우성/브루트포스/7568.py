n = int(input())
temp = []

for i in range(n):
    h, w = map(int, input().split())
    temp.append((h, w))

for i in temp:
    result = 1
    for j in temp:
        if i[0] < j[0] and i[1] < j[1]:
            result += 1
    print(result)