def hanoi_num(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi_num(n-1) + 1

def hanoi(N, start, to, via):
    if N == 1:
        print(start, to)
        return
    else:
        hanoi(N-1, start, via, to)
        print(start, to)
        hanoi(N-1, via, to, start)

if __name__=="__main__":
    num = int(input())
    # print(2**num-1)
    print(hanoi_num(num))
    hanoi(num, 1, 3, 2)