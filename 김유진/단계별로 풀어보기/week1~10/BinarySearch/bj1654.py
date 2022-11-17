'''
4 4
200
200
200
1
answer: 100

4 8
13
15
13
15
answer: 6

N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
'''
import sys
K, N = map(int, sys.stdin.readline().split())
lan = []
for _ in range(K):
    lan.append(int(sys.stdin.readline()))

low = 1
high = max(lan)
answer = 0

while low <= high:
    middle = (low + high) // 2
    total = 0
    for l in lan:
        total += l // middle

    if total >= N:
        answer = middle if answer < middle else answer
        low = middle + 1
    else:
        high = middle - 1

print(answer)