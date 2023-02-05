from collections import deque
import sys
N = int(sys.stdin.readline())
dq = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if len(command) == 2:
        if command[0] == "push_back":
            dq.append(command[1])
        else:
            dq.appendleft(command[1])
    else:
        if command[0] == "front":
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif command[0] == "back":
            if dq:
                print(dq[-1])
            else:
                print(-1)
        elif command[0] == "size":
            print(len(dq))
        elif command[0] == "empty":
            if dq:
                print(0)
            else:
                print(1)
        elif command[0] == "pop_front":
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        else:
            if dq:
                print(dq.pop())
            else:
                print(-1)

'''
문제 설명
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.


15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front

output:
2
1
2
0
2
1
-1
0
1
-1
0
3
'''
