import sys

def star(N):
    if N == 0:
        print("***")
        print("* *")
        print("***")
        return

    elif N > 3:
        print("*" * N/3)
        print("*" * (N/3)//2)
        print("*" * N/3)


N = int(sys.stdin.readline())

print("*" * (N//3))
print("*" * ((N/3)//2))
print("*" * (N//3))
