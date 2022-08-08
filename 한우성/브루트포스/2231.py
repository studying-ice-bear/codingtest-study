n = int(input())


def solve(n):
    for i in range(1, n+1, 1):
        check = i + sum(map(int, str(i)))
        if check == n:
            return i
    else:
        return 0        

print(solve(n))