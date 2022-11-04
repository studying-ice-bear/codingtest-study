from collections import defaultdict as dd
def solution(clothes):
    kinds = dd(int)

    for _, kind in clothes:
        kinds[kind] += 1
    
    answer = 1
    for k, v in kinds.items():
        answer *= v + 1
    
    answer -= 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
