import sys
N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(N):
    part = []
    for j in range(i-L+1, i+1):
        # print(i, j)
        if j < 0:
            continue
        else:
            part.append(arr[j])
    # print(part)
    answer.append(min(part))

print(*answer, sep=' ')

'''
문제
N개의 수 A1, A2, ..., AN과 L이 주어진다.
Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

12 3
1 5 2 3 6 2 3 7 3 5 2 6
output:
1 1 1 2 2 2 2 2 3 3 2 2

1 -> 1
1, 5 -> 1
1, 5, 2 -> 1
5, 2, 3 -> 
'''