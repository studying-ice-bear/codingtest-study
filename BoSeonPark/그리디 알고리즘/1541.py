import sys
input = sys.stdin.readline

word = input().strip()
a = []
flag = ''
s = ''
total = 0
for w in word:
    if w == '-':
        total += eval(flag + str(sum(list(map(int, s.split('+'))))))
        s = ''
        flag='-'
    else:
        s += w

total += eval(flag + str(sum(list(map(int, s.split('+'))))))

print(total)
