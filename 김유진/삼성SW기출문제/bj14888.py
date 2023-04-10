N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
operator = ['+', '-', '*', '/']

max_total = -int(1e10)
min_total = int(1e10)
def dfs(cnt, total, plus, minus, multiply, divide):
    global max_total, min_total

    if cnt == N:
        max_total = max(total, max_total)
        min_total = min(total, min_total)
        return

    if plus:
        dfs(cnt+1, total+numbers[cnt], plus-1, minus, multiply, divide)
    if minus:
        dfs(cnt+1, total-numbers[cnt], plus, minus-1, multiply, divide)
    if multiply:
        dfs(cnt+1, total*numbers[cnt], plus, minus, multiply-1, divide)
    if divide:
        dfs(cnt+1, int(total/numbers[cnt]), plus, minus, multiply, divide-1)

dfs(1, numbers[0], op[0], op[1], op[2], op[3])
print(max_total)
print(min_total)
