"""
- 완전 탐색
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/84512
규칙 >
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 
사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

아이디어 >
- 개수가 적기 때문에(총 3095개) 다 만들어서 정렬 ✅  thanks to 혜진님 👍👍
- 규칙 찾기(?) => 다른 사람들의 풀이 보니 규칙이 있는건 맞는듯
"""
from itertools import product

def solution(word):
    answer = 0
    keys = []
    for _ in range(1, 6):
        keys += list(map(''.join, product('AEIOU', repeat=_)))
    keys.sort()
    custom_dict = {key: i + 1 for i, key in enumerate(keys)}
    return custom_dict[word]


if __name__ =="__main__":
    word = input()
    print(solution(word))