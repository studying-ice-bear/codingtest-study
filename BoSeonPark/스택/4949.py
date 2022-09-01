import sys
input = sys.stdin.readline

def check(words):
    temp = ''
    
    pos = 0
    for w in words:
        if w == '(' or w == ')' or w == '[' or w == ']':
            temp += w
    
    n = len(temp)
    if n == 0:
        return 'yes'
    if temp[0] == ')' or temp[0] == ']':
        return 'no'
    
    while pos != len(temp)-1:
        if temp[pos:pos+2] == '()' or temp[pos:pos+2] == '[]':
            temp = temp[0:pos] + temp[pos+2:]
            pos -= 1
        else:
            pos += 1

    if len(temp) == 0:
        return 'yes'
    else:
        return 'no'
        
while True:
    s = input().rstrip()
    if s == '.':
        break
    print(check(s))

