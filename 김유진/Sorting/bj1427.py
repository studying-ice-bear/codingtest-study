import sys
in_num = sys.stdin.readline()
len_num = len(in_num) - 1
num = int(in_num)

'''
    1 10 100 100 ... 1000000000
'''
arr = []
for i in range(len_num):
    n = int(in_num[i])
    arr.append(n)

arr = sorted(arr, reverse=True)
print(' '.join(str(a) for a in arr))


'''
C++?
print(len_num)
i = 1
arr = []
for i in range(1, len_num+1):
    q = num // (10 ** i)
    r = num % (10 ** i)
    print(q, r)

'''

# while num != 0:
#     q = num // (10 * i)
#     r = num % (10 * i)
#     print(q, r)
#     arr.append()
#     i += 1