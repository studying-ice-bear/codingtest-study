"""
- 누적합

idea > 누적합을 계산할 때 
input:
a b c
d e f

↓

acc:
0 0 0 0
0 a a+b a+b+c
0 a+d a+b+d+e a+b+c+d+e+f

이런 식으로 계산 => (1,1 ~ i, j) 까지의 합

위 예에서 2행 2열 부터 2행 3열까지 합(e+f) 을 구하려면
sum = acc[2][3] - acc[1][3] - acc[2][1] + acc[1][1]

일반화
sum[si~ei][sj~ej] = acc[ei][ej] - acc[si-1][ej] - acc[ei][sj-1] + acc[si-1][sj-1]

이 때 IndexError 를 방지하기 위해 0행과 0열에 0을 추가(padding)
"""
from itertools import accumulate as A
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

acc = [[0] * (n+1) for _ in range(n + 1)]
prev = 0
for r in range(1, n+1):
    row = list(A(map(int, input().split())))
    if r == 1:
        acc[1] = [0] + row
    else:
        for c, num in enumerate(row):
            acc[r][c+1] = num + acc[r-1][c+1]
print(acc)    


for _ in range(m):
    si, sj, ei, ej = map(int, input().split())
    temp = acc[ei][ej] - acc[ei][sj-1] - acc[si-1][ej] + acc[si-1][sj-1]
    print(temp)