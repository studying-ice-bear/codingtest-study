s = input()

only_one = s.split('0')
only_zero = s.split('1')

count_one = len([i for i in only_one if len(i) != 0])
count_zero = len([i for i in only_zero if len(i) != 0])

print(min(count_one,count_zero))