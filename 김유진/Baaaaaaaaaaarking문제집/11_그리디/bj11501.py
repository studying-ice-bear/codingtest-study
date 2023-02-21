import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().split()))

    answer = 0
    max_stock = days[-1]
    for i in range(N-2, -1, -1):
        if days[i] > max_stock:
            max_stock = days[i]
        else:
            answer += max_stock-days[i]
    print(answer)

    ''' 시간 초과 코드
    max_stock = 0
    for i in range(N):
        profit = 0
        for j in range(i, N):
            if days[j]-days[i] <= 0:
                continue

            profit = days[j]-days[i] if days[j]-days[i] > profit else profit
        max_stock += profit

    print(max_stock)
    '''

'''
    미래를 미리 알기 떄문에 입력 받은 값의 뒷 순서 즉, 미래부터 값을 비교하는 게
    자료를 한 번씩 확인할 수 있어 시간을 단축시킬 수 있다.
'''