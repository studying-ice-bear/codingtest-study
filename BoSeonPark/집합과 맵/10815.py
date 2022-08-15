import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num_dict = Counter(list(map(int, input().split(' '))))

m = int(input())
num_list = list(map(int, input().split(' ')))

for num in num_list:
    if num in num_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')

"""
풀이
n개의 숫자를 dictionary의 key로 사용해 key:1 의 형태로 생성
m개의 숫자를 list로 저장하고 반복문으로 하나씩 접근해 dictionary에 존재하는지 확인
"""