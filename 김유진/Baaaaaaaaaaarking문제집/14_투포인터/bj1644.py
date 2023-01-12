import sys, math
N = int(sys.stdin.readline())

sosu = [False, False] + [True] * (N-1)
# [False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

prime_num = []

# 에라토스테네스의 체
for i in range(2, N+1):
    if sosu[i]:
        prime_num.append(i)
        for j in range(2*i, N+1, i):
            sosu[j] = False

answer = 0
start, end = 0, 0

while end <= len(prime_num):
    temp_sum = sum(prime_num[start:end])
    if temp_sum == N:
        answer += 1
        end += 1
    elif temp_sum < N:
        end += 1
    else:
        start += 1

print(answer)
