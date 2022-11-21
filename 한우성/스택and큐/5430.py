test_case = int(input())
flag = True
for i in range(test_case):
    func = input()   
    len_list = int(input())
    order_list = list(map(int, input()[1:-1].replace(",", "")))
    for order in func:
        if order == "R":
            order_list = list(reversed(order_list))
        if order == "D":
            if not order_list:
                flag = False
                break
            order_list.pop(0)
    if flag == False:
        print("error")
        break
    print(order_list)