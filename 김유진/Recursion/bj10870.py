# 피보나치 수 5
def fibonacci(order):
    if order == 0:
        return 0
    elif order == 1:
        return 1
    else:
        result = fibonacci(order-1) + fibonacci(order-2)
        return result

if __name__ == "__main__":
    num = int(input())
    print(fibonacci(num))