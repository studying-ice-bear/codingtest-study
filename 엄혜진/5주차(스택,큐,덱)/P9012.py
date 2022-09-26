import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    case = sys.stdin.readline().rstrip()
    stack = 0
    # result = True # 이거 필요없구나!

    for i in range(len(case)):
        # if stack > 0:
        #     result = False
        #     break 여기 말고 )를 더할 때 확인해도 되는구나!

        if case[i] == '(':
            stack -= 1
        elif case[i] == ')':
            stack += 1
            if stack > 0:
                break

    # if stack != 0:
    #     result = False

    if stack == 0:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
