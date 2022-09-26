"""
- 누적합

idea > 누적합 배열을 구하고 각 value를 m으로 나눈 나머지가 같은 것들을 2개씩 뽑는 조합을 계산
구간합은 누적합 배열 요소의 차를 통해 계산하기때문에 (EX. a[i] ~ a[j] 합 = S[j] - S[i-1])
m으로 나눈 나머지가 같아야 뺐을 때 0이 나옴 => 나누어 떨어짐

ex
input:
5 3
1 2 3 1 2

acc = [0, 1, 3, 6, 7, 9]
acc % 3 = [0, 1, 0, 0, 1, 0]
0 : 4개
1 : 2개
4C2 = 6
2C2 = 1
===> 개수 : (6+1) = 7개
"""

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = defaultdict(int)
sub_total = 0
for _ in range(n+1):
    cnt[sub_total % m] += 1
    if _ < n:
        sub_total += arr[_]

# print(cnt)
answer = 0
for value in cnt.values():
    answer += ((value) * (value - 1) // 2)  # math.comb(value, 2)

print(answer)

"""
★ 알아두면 좋을 메소드
itertools.accumulate : 누적합을 구해줌 
math.comb(a, b) : aCb 값을 구해줌
"""