n, m = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
end = 0
interval_sum = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += numbers[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= numbers[start]

print(count)

'''
처음에 풀이할 때는 start, end를 두고 완전탐색해서 O(N^2)으로 풀이함. 
-> 그래서 O(N)으로 풀기 위해서 다음 알고리즘으로 풀이
'''