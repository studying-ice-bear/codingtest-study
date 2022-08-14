import sys
f = sys.stdin.readline

n = int(f())
move_list = []
def move(start, to):
    move_list.append((start, to))
    

def hanoi(n, start, to, via): # 1, 3, 2
    if n == 1:
        move(start, to)
    else:
        hanoi(n-1, start, via, to) # 1, 2, 3
        move(start, to)
        hanoi(n-1, via, to, start)
        
hanoi(n, 1, 3, 2)

print(len(move_list))

for s, t in move_list:
    print(s, t)