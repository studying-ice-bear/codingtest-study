n, k = map(int,input().split())
a = sorted([int(input()) for i in range(n)], reverse=True)
count = 0
for i in a:
    count += k // i
    k = k % i
print(count)