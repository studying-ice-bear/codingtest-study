import sys
N = int(sys.stdin.readline())
ppl = {}

for _ in range(N):
    name, action = sys.stdin.readline().strip().split()

    if action == "enter" :
        ppl[name] = action
    else:
        ppl.pop(name)

print(*sorted(ppl, reverse=True), sep='\n')

'''
시간 초과: https://www.acmicpc.net/board/view/80812

4
Baha enter
Askar enter
Baha leave
Artem enter

3
Baha enter
Baha leave
Baha enter


3
Aha enter
Bana enter
Cat enter

'''