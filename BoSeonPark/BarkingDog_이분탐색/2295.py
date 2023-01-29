import sys
input = sys.stdin.readline

n = int(input())
answer = 0
u = []

for _ in range(n):
    u.append(int(input()))

u.sort()
u_sum = set()
flag = False

for i in u:
    for j in u:
        u_sum.add(i+j)
        

for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if u[i] - u[j] in u_sum:
            answer = u[i]
            flag = True
            break
    
    if flag:
        break
print(answer)

"""
x + y = k - z
"""
    