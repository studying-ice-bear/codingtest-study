def hanoi(n, start, to):
    if n == 1:
        print(start, to)
        return
    # 1, 2, 3
    # 1+2+3 = 6

    hanoi(n-1, start, 6-start-to)
    print(start, to)
    hanoi(n - 1, 6 - start - to, to)

if __name__ == "__main__":
    num = int(input())
    print(2**num-1)
    hanoi(num, 1, 3)