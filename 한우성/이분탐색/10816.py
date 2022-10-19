import sys

N = int(sys.stdin.readline())
N_list = list(map(str, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(str, sys.stdin.readline().split()))
hash = {}
result = []

for i in N_list:
    try: hash[i] += 1
    except: hash[i] = 1

for i in M_list:
    try: result.append(hash[i])
    except: result.append(0)

print(*result)


