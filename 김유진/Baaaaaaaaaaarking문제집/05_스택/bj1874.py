import sys
N = int(sys.stdin.readline())
stack = []
answer = []
curr = 1
cant = True
for _ in range(N):
    num = int(sys.stdin.readline())

    while curr <= num:
        stack.append(curr)
        answer.append('+')
        curr += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        cant = False
        break

if cant:
    print(*answer, sep='\n')
