from collections import defaultdict 

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

end = 0
num_dict = defaultdict(int)
result = 0

for start in range(n):
    while end < n:
        if numbers[end] in num_dict:
            num_dict[numbers[end]] += 1
        else:
            num_dict[numbers[end]] = 1

        if num_dict[numbers[end]] > k:
            num_dict[numbers[end]] -= 1
            break
        end += 1

    temp = end - start
    if temp > result: result = temp 
    num_dict[numbers[start]] -= 1

print(result)

'''
반례
21 1
1 2 3 4 5 6 6 7 8 9 10 11 13 15 63 34 34 33 33 22 1
output : 10
'''