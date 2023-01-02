import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline())

# print(arr)
for a in arr:
    answer = "YES"
    stack = []
    for i in range(len(a)):
        # print(a[i], stack)
        if a[i] == '(':
            stack.append(a[i])
        elif a[i] == ')':
            if not stack:
                answer = "NO"
                break
            stack.pop()
        else:
            if stack:
                answer = "NO"
            break


    print(answer)