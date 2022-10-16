from itertools import combinations

'''
    시간초과
'''
def solution(number, k):
    answer = ''
    get = len(number) - k
    numbers = [int(n) for n in number]
    combos = []

    for num in combinations(numbers, get):
        combo = ''
        for n in num:
            combo += str(n)
        # print(combo)
        combos.append(combo)

    answer = max(combos)

    return answer