import sys
N = int(sys.stdin.readline())
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline())

stack = []
j = 0
i = 0
result = ""

while True:
    if not stack:
        for k in range(1, arr[i]+1):
            stack.append(k)
            result += "+\n"
        j = arr[i]

    else:
        if i >= len(arr):
            break

        if j < arr[i]: # j < arr[i]
            for k in range(j+1, arr[i] + 1):
                stack.append(k)
                result += "+\n"

            if j < arr[i]:
                j = arr[i]

        check = True
        num = len(stack)
        while num:
            num -= 1
            result += "-\n"
            n = stack.pop()
            print(stack, arr[i])
            if arr[i] == n:
                i += 1
                check = False
                break

        if not stack and j == len(arr):
            break

        if check:
            result = "NO"
            break

print(result)






