n = int(input())
table = [(0,0)]

d = [0] * 16

for i in range(n):
    t, p = map(int, input().split())
    table.append((t,p))

# print(table)

for i in range(n, 0, -1):

    if i + table[i][0] <= n+1:
        d[i] = table[i][1]
        next = i + table[i][0]
        # next = 9
    else:
        continue
    max_num = 0
    if next <= n:
        for idx in range(next,n+1):
            if d[idx] > max_num:
                max_num = d[idx]
        d[i] += max_num

# print(d)
print(max(d)) 