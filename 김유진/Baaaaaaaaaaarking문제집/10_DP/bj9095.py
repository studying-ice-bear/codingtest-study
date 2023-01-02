import sys
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    dp = [0] * 11

    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n-1])

'''
문제 링크: https://www.acmicpc.net/problem/9095
    n: 1
    합: 1
    총 1개

    n: 2
    합: 1+1, 2
    총 2개

    n: 3
    합: 1+1+1, 1+2, 2+1, 3
    총 4개

    n: 4
    합: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
    총 7개
    n(3)+1 :
        (1+1+1)+1, 1+(1+2), 1+(2+1), 3+1
    n(2)+2:
        (1+1)+2, 2+2
    n(1)+3:
        1+3

참고: https://jyami.tistory.com/15
'''