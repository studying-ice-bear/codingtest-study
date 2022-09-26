import sys

N = int(sys.stdin.readline().rstrip())

recursion_cnt = 0


def fibo_recursion(n):
    global recursion_cnt

    if n == 1 or n == 2:
        return 1
    else:
        return fibo_recursion(n - 1) + fibo_recursion(n - 2)

recursion_cnt = fibo_recursion(N) # N이 1이나 2가 될때 까지 재귀하기 때문에 코드1의 실행횟수를 계산하는 것은 피보나치 수열을 접근하는 것과 같다.

dp_cnt = N - 2

# def fibo_dp(n):
#     global dp_cnt
#
#     f = [0, 1, 1]
#     for i in range(3, n + 1):
#         dp_cnt += 1
#         f.append(f[i - 1] + f[i - 2])
#     return f[n]

# fibo_dp(N)

print(recursion_cnt, dp_cnt)

# python3으로 실행하면 시간초과가 나고 pypy3으로 실행하면 맞았다고 나온다.
# 둘의 차이를 알아보니,
# 출저: https://ralp0217.tistory.com/entry/Python3-%EC%99%80-PyPy3-%EC%B0%A8%EC%9D%B4
# pypy3는 JIT방식(Just In Time, python3처럼 실행하기 전에 파일 전체를 컴파일하지 않고 실행시점에 필요한 부분을 즉석으로 컴파일 하는 방식)
# 로 컴파일을 하고, 자주 쓰이는 코드를 캐싱하기 때문에 python3보다 빠르다.