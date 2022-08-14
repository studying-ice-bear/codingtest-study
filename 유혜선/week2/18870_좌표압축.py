"""
- 원소별로 해당 원소보다 작은 원소의 개수로 변경
- ex [1, 2, 3, 8, 5, 2, 3] => [0, 1, 2, 4, 3, 1, 2]
- 주어진 배열을 set()으로 형변환해서 중복을 없앤 뒤 정렬을 하면 정렬한 배열의 인덱스가 해당 숫자보다 작은 수의 개수가 됨
- ex 
[1, 2, 3, 8, 5, 2, 3] => set(1, 2, 3, 8, 5) 
=> [1(0), 2(1), 3(2), 5(3), 8(4)]
=> [0, 1, 2, 4, 3, 1, 2]

"""
import sys

input = sys.stdin.readline

n = int(input())

num_arr = list(map(int, input().split()))
num_idx = {y: x for x, y in enumerate(sorted(list(set(num_arr))))}

for i in range(len(num_arr)):
    print(num_idx[num_arr[i]], end=" ")
