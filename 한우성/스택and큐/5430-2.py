from collections import deque

test_case = int(input())

for i in range(test_case):
    func = input()   
    len_list = int(input())
    order_list = input()[1:-1].split(',')
    queue = deque(order_list) 
    flag = 0

    if len_list == 0:
        queue = []

    for function in func:
        if function == "R":
            flag += 1
        elif function == "D":
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0: # 짝수 뒤집히면 원래대로 왼쪽 빼기
                    queue.popleft()
                else: # 홀수 뒤집히면 오른쪽 뺴기
                    queue.pop()

    else:
        if flag % 2 == 0 :
            print("[" + ",".join(map(str, queue)) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(map(str, queue)) + "]")