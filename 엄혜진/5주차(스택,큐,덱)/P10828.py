import sys

n = int(sys.stdin.readline().rstrip())
s = []
for _ in range(n):
    line = sys.stdin.readline().rstrip().split()
    action = ""
    x = 0
    if len(line) > 1:
        action = line[0]
        x = int(line[1])
    else:
        action = line[0]

    if action == "push":
        s.append(x)
    elif action == "pop":
        if len(s) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(s[len(s) - 1]) + '\n')
            s = s[:-1]
    elif action == "size":
        sys.stdout.write(str(len(s)) + '\n')
    elif action == "empty":
        if len(s) == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif action == "top":
        if len(s) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(s[len(s) - 1]) + '\n')

# 30840	80