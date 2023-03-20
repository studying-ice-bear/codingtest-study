n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = 0

for i in range(n):
    min_num = min(a)
    max_num = max(b)
    s += (min_num * max_num)
    a.remove(min_num)
    b.remove(max_num)

print(s)