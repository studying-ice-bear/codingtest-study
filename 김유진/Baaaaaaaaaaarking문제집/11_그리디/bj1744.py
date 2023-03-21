import sys
N = int(sys.stdin.readline())
negative = []
positive = []
zero = False
total = 0

for _ in range(N):
    a = int(sys.stdin.readline())
    if a < 0:
        negative.append(a)
    elif a == 0:
        zero = True
    elif a == 1:
        total += 1
    else:
        positive.append(a)

positive.sort(reverse=True)
negative.sort()

if len(positive) > 0:
    for i in range(0, len(positive)-1, 2):
        total += positive[i] * positive[i+1]

if len(positive) % 2 != 0:
    total += positive[-1]

if len(negative) > 0:
    for i in range(0, len(negative)-1, 2):
        total += negative[i] * negative[i+1]

if len(negative) % 2 != 0:
    if not zero:
        total += negative[-1]

print(total)

'''
양수는 양수끼리 곱함
0은 음수랑 곱하면 상쇄된다. -> 가장 큰 음수값이랑 곱함.
음수는 음수끼리 곱하면 최대값
1은 곱하면 곱한 수의 값이 되기 때문에 1은 그냥 더하기
'''