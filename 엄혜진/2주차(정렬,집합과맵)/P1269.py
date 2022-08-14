import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

set1 = set(list(map(int, sys.stdin.readline().rstrip().split())))
set2 = set(list(map(int, sys.stdin.readline().rstrip().split())))

set1_set2 = len(set1 - set2)
set2_set1 = len(set2 - set1)
# set 차집합
# Doc: https://docs.python.org/3/library/stdtypes.html?highlight=set#frozenset.difference

answer = set1_set2 + set2_set1
sys.stdout.write(str(answer))
