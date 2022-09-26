import sys

N = int(sys.stdin.readline())
N_list = list(map(str, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(str, sys.stdin.readline().split()))
hash = {}

for i in N_list:
    hash[i] = 1

for i in M_list:
    try: print(hash[i])
    except: print(0)


