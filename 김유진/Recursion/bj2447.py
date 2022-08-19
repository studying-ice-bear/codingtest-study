def star(N):
    if N == 3:
        print("***")
        print("* *")
        print("***")
    elif N > 3:
        star(N-3)

star(3)