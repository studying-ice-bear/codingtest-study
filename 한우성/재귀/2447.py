n = int(input())

def solve(n):
    k = n//3
    for i in range(k):
        print(n*"*")
        print(k*"*" + k*" " + k*"*")
    print(n*"*")

solve(n)