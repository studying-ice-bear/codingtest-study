import sys
'''
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
'''

def fib(n):
    if n == 1 or n== 2:
        return 1
    return fib(n-1) + fib(n-2)

'''
fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
'''
def fibonacci(n):
    arr = [0]*(n+1)
    arr[1], arr[2] = 1, 1
    execution = 0
    for i in range(3, n+1):
        execution += 1
        arr[i] = arr[i-1] + arr[i-2]
    return arr, execution

N = int(sys.stdin.readline())
print(fib(N), fibonacci(N)[1])