import sys

input = sys.stdin.readline

s = input().rstrip()

while s != '.':
    result = True
    i = 0
    stack = []
    while s[i] != '.':
        # if s[i] == '(':
        #     stack.append('(')
        # elif s[i] == '[':
        #     stack.append('[')
        # 위 표현을 아래처럼 한게 신기했다
        if s[i] in '([':
            stack.append(s[i])
        # elif s[i] == ')':
        #     if len(stack) < 1 or stack[-1] != '(':
        #         result = False
        #         break
        #     else:
        #         stack.pop()
        # elif s[i] == ']':
        #     if len(stack) < 1 or stack[-1] != '[':
        #         result = False
        #         break
        #     else:
        #         stack.pop()
        # 위에 in을 사용한거처럼 닫는 괄호를 처리하는 방식도 변경할 수 있다
        elif s[i] in ')]':
            if len(stack) == 0 or (stack.pop() + s[i]) not in ('()', '[]'):
                result = False
                break

        i += 1
    # print(stack)
    if result and len(stack) == 0:
        print('yes')
    else:
        print('no')
    s = input().rstrip()

# 30840KB	140ms
# 보기 좋게 변경했으나 메모리를 줄이거나 시간을 절약하진 못했다..