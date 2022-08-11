import sys

N = int(input())

nums = [0] * 10001 # 100000 도 입력될 수 있다는 것을 잊지 말자

for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for _ in range(nums[i]):
            sys.stdout.write(str(i) + "\n")
