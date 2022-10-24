"""
- 투 포인터

idea> 부분합 체크!
- 두개의 포인터는 맨 처음부터 시작한다! 어차피 배열 끝까지 탐색해야되므로 end포인터(p2)는 for문으로 해줌
- 차례대로 sub_total을 구해준 후, sub_total >= s 가 되는 경우 p1 포인터를 하나씩 땡겨준다. (조건을 만족하는 최소 길이를 구해야 하므로)
- p1을 땡기다가 sub_total < s 가 되는 경우 다시 p2 포인터를 증가시킨다.
- p1, p2 모두 n-1이 되면 탐색 종료
"""
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = n + 1
p1 = 0
sub_total = 0
for p2 in range(n):
    sub_total += arr[p2]

    while sub_total >= s and p1 <= p2:
        answer = min(answer, p2 - p1 + 1)
        sub_total -= arr[p1]
        p1 += 1

print(answer if answer != n+1 else 0)
