import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    stock = list(map(int, sys.stdin.readline().split()))

    # 1. 시간초과
    # 원인: 최댓값인 날이 지나면 다시 최댓값을 찾아야한다.

    # sell = max(stock)

    # answer = 0
    # buy = 0
    # cnt = 0
    # pre = 0
    # for i in range(n):
    #     if stock[i] < sell:
    #         buy += stock[i]
    #         cnt += 1
    #     elif stock[i] == sell:
    #         answer += stock[i] * cnt - buy
    #         buy = 0
    #         cnt = 0
    #         if i < len(stock) - 1:
    #             sell = max(stock[i + 1:])
    # print(answer)


    # 2.
    # https://www.acmicpc.net/board/view/16527 에 달린 답글의 로직대로 했더니 시간안에 해결할 수 있었다.
    answer = 0
    maximum = 0

    for i in range(len(stock)-1, -1, -1):
        if stock[i] > maximum:
            maximum = stock[i]
        else:
            answer += maximum - stock[i]

    print(answer)