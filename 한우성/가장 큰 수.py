import functools

def sort_num(a, b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    sort_list = [str(x) for x in numbers]
    answer = sorted(sort_list,key = functools.cmp_to_key(sort_num), reverse = True)
    
    return str(int("".join(answer)))
# functools 을 사용해서 함수에 인자 두개를 넘겨주는 방식으로 key값 정렬

def solution(numbers):
    sort_list = list(map(str, numbers))
    sort_list.sort(key = lambda x : x * 3, reverse = True)
    return "".join(sort_list)
# 혹은 그냥 아스키 코드로 문자열 정렬 