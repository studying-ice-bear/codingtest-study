import math
import sys
import itertools

N = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

ops_basic = ['+', '-', '*', '/']
op_count = list(map(int, sys.stdin.readline().rstrip().split()))
ops = []
for i in range(len(op_count)):
    for j in range(op_count[i]):
        ops.append(ops_basic[i])

# print(nums, op_count, ops)

result_max = -math.inf
result_min = math.inf

cases = list(set(list(itertools.permutations(ops, N - 1))))

for case in cases:
    total = nums[0]
    for i in range(1, N):
        if case[i - 1] == '+':
            total += nums[i]
        elif case[i - 1] == '-':
            total -= nums[i]
        elif case[i - 1] == '*':
            total *= nums[i]
        elif case[i - 1] == '/':
            if total < 0:
                total *= -1
                total //= nums[i]
                total *= -1
            else:
                total //= nums[i]

    if result_max < total:
        result_max = total
    if result_min > total:
        result_min = total

sys.stdout.write(str(result_max) + '\n')
sys.stdout.write(str(result_min) + '\n')

# 시간초과가 나서 검색해보니(https://www.acmicpc.net/board/view/86187)
# 연산자 순열이 중복되는 경우가 있었다.
# set()으로 중복되는 경우의 수를 제거해줬다.
