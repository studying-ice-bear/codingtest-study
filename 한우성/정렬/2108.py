import sys
from collections import Counter

input_list = []

for i in range((int(sys.stdin.readline()))):
    input_list.append((int(input())))

input_list.sort()

def solve(input_list):
    mid = len(input_list) // 2
    print(round(sum(input_list) / len(input_list)))
    print(input_list[mid])
    print(mode(input_list))
    print(range(input_list))


def mode(input_list):
    counted_list = Counter(input_list).most_common()
    max = counted_list[0][1]
    # modes = []
    # for i in counted_list:
    #     if i[1] == max:
    #         modes.append(i[0])  
    # if len(modes) >= 2:
    #     modes.sort()
    #     return modes[1]
    # return modes[0]
    if len(counted_list) > 1:
        if max == counted_list[1][1]:
            return counted_list[1][0]
        else:
            return counted_list[0][0]
    else:
        return counted_list[0][0]

def range(input_list):
    max_num = max(input_list)
    min_num = min(input_list)
    return max_num - min_num

solve(input_list)