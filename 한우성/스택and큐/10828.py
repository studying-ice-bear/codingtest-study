import sys

N = int(sys.stdin.readline())
check_list = []

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        check_list.append(order[1])
    if order[0] == 'pop':
        if(len(check_list) > 0):
            print(check_list.pop())
        else:
            print(-1)
    if order[0] == 'size':
        print(len(check_list))
    if order[0] == 'empty':
        if len(check_list) == 0:
            print(1)
        else:
            print(0)
    if order[0] == 'top':
        if len(check_list) > 0:
            print(check_list[-1])
        else:
            print(-1)