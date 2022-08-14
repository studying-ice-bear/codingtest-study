"""
- 카드를 딕셔너리에 키값으로 저장하고 이후 입력받은 숫자를 검사
- 검사하는 로직이 있는 변수 => check
"""
import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
card_dict = {x: True for x in cards}

m = int(input())
check = list(map(lambda x: 1 if (int(x) in card_dict) else 0, input().split()))

print(*check, sep=" ")