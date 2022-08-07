n = int(input())

def hanoi(n, a, b, c): # n개의 원반을 a에서 c로 이동하는데 b를 보조로 사용해라.
    if n == 1:
        print(a, c) # a에 있는 원반을 c로 이동
    else:
        hanoi(n - 1, a, c, b) # 가장 아래의 원반을 제외한 n-1개의 원반을 a에서 b로 옮긴다.
        print(a, c) # a에 있는 원반을 c로 이동
        hanoi(n - 1, b, a, c) # n-1개의 원반을 b에서 c로 옮긴다.

# 하노이는 여전히 이해가 될듯 하면서도 안된다.. 이론은 이해가 가도 코드로 도출하는게 어렵다.
# 실제로 이런 문제가 나오면 풀 수 있을까?

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1

print(sum)
hanoi(n, 1, 2, 3)
