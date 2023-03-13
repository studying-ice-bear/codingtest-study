import sys
N = int(sys.stdin.readline())
U = set()
for _ in range(N):
    U.add(int(sys.stdin.readline()))
'''
list_U = list(U)
sum_list = []

for i in range(N):
    for j in range(i, N):
        if 

print(sum_list)
'''

def bs(arr, total):
    left, right = 0, len(arr)-1
    check = False
    print(arr, len(arr))

    while left <= right:
        if right > len(arr)-1 or left > len(arr)-1:
            break

        if total == (arr[left] + arr[right]):
            check = True
            break
        elif total < arr[left] + arr[right]:
            left += 1
        else:
            right += 1

    if check:
        return left, right
    else:
        return -1, -1


U = list(U)
answer = 0

print(U)
for i in range(len(U)):
    u = U[i]
    new = U.copy()
    new.remove(u)

    for j in range(len(U)-1):
        limit = new[j]
        print(i, u, " 고정")
        x, y = bs(new, limit-u)
        print(x, y)

        if x != -1 and y != -1:
            answer = max(answer, limit+u)


'''
5
2
3
5
10
18

x + y + z = k
x + y = k - z
'''