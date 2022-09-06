import sys
N = int(sys.stdin.readline())
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline())

stack = []
j = 0
i = 0
result = []

while True:
    print(i, stack, arr[j])
    if result:
        if result[-1] < i:
            print("NO")
            break

    if i < arr[j]:
        if result[-1] < i:
            print("NO")
            break
        for k in range(i+1, arr[j]+1):
            print("+")
            stack.append(k)
        print(stack)
        result.append(stack.pop())
        print("-")
        i = arr[j]
    else:
        stack.pop()
        print("-")
    j += 1
