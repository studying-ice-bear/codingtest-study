import sys
input = sys.stdin.readline

def check(bracket):
    stack = []
    
    for b in bracket:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop()
    
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

n = int(input())

for _ in range(n):
    s = input().strip()
    print(check(s))