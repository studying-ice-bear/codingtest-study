import sys
input = sys.stdin.readline

n = int(input())
pos = list(map(int, input().split(' ')))

pos_dict = {val : i for i, val in enumerate(sorted(set(pos)))}

for p in pos:
    print(pos_dict[p], end=' ')

"""
풀이
오름차순으로 정렬 후 정렬된 배열에서 각값에 대한 인덱스 값을 dictionary로 만든다.
* 중복된 값의 경우 제일 낮은 인덱스 값만 유지
정렬전의 원본 배열에 있는 원소 값들을 key로 사용해 dictionary에서 값을 가져와 각각의 값을 바꿔준다.
"""