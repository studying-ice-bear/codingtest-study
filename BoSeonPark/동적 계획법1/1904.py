import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

a = 1
b = 2
answer = 0

for i in range(2, n):
    answer = (a + b) % 15746
    a = b
    b = answer

print(answer)