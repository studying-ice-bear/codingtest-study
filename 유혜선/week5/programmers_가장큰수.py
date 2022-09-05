"""
- 정렬
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/42746
규칙 >
숫자 배열이 주어질때 조합해서 가장 큰 수를 만들어라

아이디어 > 
1) 큰 수를 만들려면 "문자열"로 정렬해야 한다.
⭐ 2) ["3", "34", "30"] => "34330" 가 되어야 하지만 
정렬하면 ["34", "30", "3"]
=> 정렬할때는 자릿수를 맞춰서 해줘야 한다.
["33(3)", "34", "30"] => ["34", "33(3)", "30"] => "34330"

문제에서 0 ≤ x ≤ 1000 이므로 자릿수는 3개로 맞춰주면 다 비교할 수 있다.

"""
def solution(numbers):
    answer = ""
    new_array = list(map(lambda x: [(str(x)*4)[:4], len(str(x))], numbers))
    new_array.sort(reverse=True)
    for val, l in new_array:
        answer += val[:l]
    return str(int(answer))


"""
# js식 풀이 ㅋㅋ 
functools.cmp_to_key : sort()의 key로 함수를 넘겨줄때 사용 (이때 이 함수는 인자를 2개 사용하는 비교함수)
설명: https://wikidocs.net/109303

* js에서는 sort의 key에 매개변수를 2개받는 함수를 넣어줌

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
"""

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))