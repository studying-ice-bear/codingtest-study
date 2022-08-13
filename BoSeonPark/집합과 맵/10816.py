import sys
from collections import Counter
input = sys.stdin.readline


n = int(input())
left = Counter(list(map(int, input().split())))

m = int(input())
right = list(map(int, input().split()))

for r in right:
    print(left.get(r, 0), end = ' ')
    
"""
풀이
처음 n개의 숫자는 dictionary로
두 번째 m개의 숫자는 list로 저장
list로 저장된 숫자들을 반복문을 사용해 하나씩 key로 사용해 dictionary에 존재하는지 확인하고
없으면 0, 있으면 해당 값을 출력
"""