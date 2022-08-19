n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

for num in sorted(nums):
    print(num)
# sorted(iterable, /, *, key=None, reverse=False)
# Doc: https://docs.python.org/3/library/functions.html?highlight=sorted#sorted
# 이터러블 객체를 정렬하여 새 배열로 반환한다.

# 다른 방법: list.sort(*, key=None, reverse=False)
# Doc: https://docs.python.org/3/library/stdtypes.html?highlight=list%20sort#list.sort
# 리스트를 정렬한다.

# nums.sort()
# for num in nums:
#     print(num)
