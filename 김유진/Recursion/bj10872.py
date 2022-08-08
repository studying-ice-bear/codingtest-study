def factorial(num):
    if num == 0:
        return 1
    else:
        result = num * factorial(num-1)
    return result

if __name__ == "__main__":
    num = int(input())
    print(factorial(num))