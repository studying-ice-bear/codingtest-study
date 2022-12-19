import itertools
import sys

l, c = map(int, sys.stdin.readline().rstrip().split())
ch = list(sys.stdin.readline().rstrip().split())

ch.sort()

arr = list(itertools.combinations(ch, l))
for a in arr:
    vowel_flag = False
    consonant_cnt = 0
    for c in a:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel_flag = True
        else:
            consonant_cnt += 1

        if consonant_cnt >= 2 and vowel_flag:
            break

    if vowel_flag and consonant_cnt >= 2:
        print(''.join(a))
