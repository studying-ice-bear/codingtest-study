import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(arr)
sum = 0
left = []
prefix = []
for a in arr:
    sum += a
    prefix.append(sum)
    left.append(sum % M)

print(prefix)
print(left)

answer = 0
com = []
for i in range(M):
    for l in left:
        if l == i:
            com.append(i)
    print(com)
    answer += len(list(combinations(com, 2)))
    print(answer)

print(list(combinations([1, 1, 1], 2)))
'''
input: 
5 3
1 2 3 1 2
output:
7

hint
[1, 3, 6, 7, 9] = [1, 1+2, 1+2+3, 1+2+3+1, 1+2+3+1+2]
[1/3=0...1, (1+2)/3 =1....0, (1+2+3)/3=2...0, (1+2+3+1)/3=2....1, (1+2+3+1+2)/3=3....0] 
2번째랑 3번째랑 마지막이 나머지가 0이니까
그 세 가지 중에 두 개 사이의 값을 빼도 나머지가 0
(1+2+3+1)/3=2....1,랑
1/3=0...1랑
빼면 0
2C2
'''