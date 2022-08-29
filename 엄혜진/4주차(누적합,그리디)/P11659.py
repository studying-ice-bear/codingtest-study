import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))

pre_sum = [0]
temp = 0
for num in nums:
    temp += num
    pre_sum.append(temp)
# print(pre_sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    # sys.stdout.write(str(sum(nums[i - 1:j])) + '\n') # 입력 할 때 마다 누적합을 구하기 때문에 O(n^2)의 시간복잡도를 보인다. dp로 진행!
    sys.stdout.write(str(pre_sum[j] - pre_sum[i - 1]) + '\n')
