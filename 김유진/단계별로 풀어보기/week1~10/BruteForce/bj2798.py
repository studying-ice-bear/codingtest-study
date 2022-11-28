import sys
cnt, sum = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))
print(cnt, sum)
print(arr)

reversed_arr = sorted(arr, reverse=True)

total = 0
visited = [0 for _ in range(cnt)]

sum_list = [] # 3장을 뽑아서 넣음
total_list = []

for i in range(cnt):
    if len(sum_list) == 3:
        print(sum_list)
        total = sum(sum_list)
        total_list.append(total)
        sum_list = []
    start = arr.index(sum_list[-1]) + 1 if sum_list else 0
    for next in range(start, len(arr)):
        sum_list.append(arr[next])

print(total_list)






