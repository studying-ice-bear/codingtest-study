import sys

n = int(input())
nums = []
# for _ in range(n):
#     nums.append(int(input()))

# nums.sort()
# for num in nums:
#     print(num)

# 새 배열을 만드는 sorted보다 sort를 쓰면 메모리를 효율적으로 쓸 수 있을거라 기대했는데, 시간초과가 났다.

# ---------------------------

# O(nlogn) 의 시간 복잡도를 가지는 힙을 사용해 보겠다.
# Doc: https://docs.python.org/3/library/heapq.html?highlight=heap#module-heapq

# import heapq
#
# for _ in range(n):
#     heapq.heappush(nums, int(input()))
#
# for i in range(len(nums)):
#     print(heapq.heappop(nums))

# 시간초과가 난다.

# ---------------------------

# 결국 검색했다..
# 원인은 input()이었다.

# input VS. sys.stdin.readline
# 1. input()은 prompt message를 출력하는 기능도 있어서, 백만번 입력을 받으면 부하가 온다.
# (물론 prompt message를 전달하진 않았지만 부하가 올 수 있다고 한다.)
# 2. input()은 입력받은 값의 개행문자를 삭제시켜서 리턴한다.
# 입력받은 값이 str, 즉 mutable한 값이기 때문에 개행문자를 삭제시킨 문자열을 새로 만들어서 반환할 것이다. 즉, 비효율적인 메모리 사용이다.

# Python Immutable type And Mutable type
# Immutable type: int, float, str, tuple
# Mutable type: list, dict

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
for num in nums:
    print(num)