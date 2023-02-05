from collections import deque
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    do = sys.stdin.readline().strip()
    N = int(sys.stdin.readline())
    p = sys.stdin.readline().rstrip().replace("[", "").replace("]", "")
    if N == 0:
        dq = deque()
    else:
        p = list(p.split(","))
        dq = deque(p)

    error = False
    turn = 0
    for d in do:
        if d == 'R':
            turn += 1
        else:
            if dq:
                if turn % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                error = True
                break
    if error:
        print('error')
    else:
        if turn % 2 != 0:
            dq.reverse()
        print("[" + ",".join(dq) + "]")
        # print(list(dq))

'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
output:
[2,1]
error
[1,2,3,5,8]
error

testcase2:
1
DD
1
[42]
output:
error

testcase3:
1
RDD
4
[1,2,3,4]
output:
[2,1]

**** 문제 풀이 ****
1. reverse를 매번 실행하면 시간 초과
2. 출력은 ,(콤마)뒤에 띄어있지 않다 -> 내가 따로 출력문 생성
*****************
'''