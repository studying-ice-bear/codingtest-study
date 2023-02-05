import sys

n = int(sys.stdin.readline().rstrip())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())

# print(n, budget, m)

max_budget = max(budget)


def find_highest_budget():
    result = 0
    left, right = 1, max_budget
    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for i in range(n):
            temp += min(budget[i], mid)

        if temp <= m:
            result = max(result, mid)
            left = mid + 1
        else:
            right = mid - 1
    return result


if sum(budget) <= m:
    print(max_budget)
else:
    print(find_highest_budget())
