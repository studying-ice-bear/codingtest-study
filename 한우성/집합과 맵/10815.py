import sys

n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
check_num = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

def solve(i):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == i:
            return 1

        elif n_list[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in check_list:
    print(solve(i), end = " ")



