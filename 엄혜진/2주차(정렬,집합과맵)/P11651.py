N = int(input())

plain = []

for i in range(N):
    point = list(map(int, input().split()))
    plain.append(point)

plain.sort(key=lambda p: [p[1], p[0]])

for i in plain:
    print(i[0], i[1])