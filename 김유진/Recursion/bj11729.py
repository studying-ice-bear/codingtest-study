def hanoi_num(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi_num(n-1) + 1
def hanoi(start, end, n):
    if(end == 1):
        print(start, end)
    # 빈 원반이 1, 2, 3 중 하나이고 서로 다르다.
    # start + end + empty = 1+2+3 = 6
    empty = 6-start-end
    print(empty)
    hanoi(start, empty, n-1)
    print(start, end)
    hanoi(empty, end, n-1)

if __name__=="__main__":
    num = int(input())
    print(2**num-1)
    # hanoi(1, 3, num)