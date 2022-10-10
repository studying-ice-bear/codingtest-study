"""
- 그리디 (탐욕법)
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/42860
규칙 >
"A"로 초기화된 문자열을 입력 받은 문자열(name)로 바꾸기 위해 버튼을 누르는 최소 횟수를 구하세요.

아이디어 >
[ 문자열 바꾸기 ]
- A to N : ▲ 방향 버튼 누르기
- O to Z : ▼ 방향 버튼 누르기

[ 이동하기 ]
- 이동 방법은 아래 4가지라고 생각하면 됨
    1) 계속 오른쪽으로 움직이기
    2) 계속 왼쪽으로 움직이기
    3) 오른쪽으로 가다가 다시 왼쪽으로 움직이기
    4) 왼쪽으로 가다가 다시 오른쪽으로 움직이기
    😑 최소 횟수를 구해야하기 때문에 두번 이상 방향을 바꿀 필요 x

- 'A'가 아닌 글자들의 위치를 구하고, i번째와 i+1번째를 어떤 방향으로 움직여야 빠른지 계산
    - 'A'가 아닌 글자는 다 바꿔야되기 때문에 i번째 원소까지 움직였다면 반대로 움직일땐 i+1까지 진행해야함
    - ex. ['A', 'B', 'B', 'A', 'B'] => [(1, 'B'), (2, 'B'), (4, 'B')]
        - 0번부터 4번까지 오른쪽으로 쭉 이동
        - 4번부터 1번까지 왼쪽으로 쭉 이동
        - 1번까지 오른쪽으로 갔다가 처음으로 돌아온후 4번에서 2번까지 왼쪽으로 이동
        - 4번에서 2번까지 왼쪽으로 이동했다가, 다시 4번으로 돌아온 후(오른쪽 방향 이동) 0번에서 1번까지 이동
        - 2번까지 오른쪽으로 갔다가 처음으로 돌아온후 4번까지 왼쪽으로 이동
        - 4번으로 갔다가(왼쪽 방향 이동) 처음부터 2번까지 오른쪽으로 이동
        위 경우 중 최솟값을 구해서 위아래버튼 최솟값과 더하면 됨.

"""
def solution(name):
    answer = 999
    num_list = [ord(c) - 65 if ord(c) <= 78 else 91 - ord(c) for c in name]
    
    # case 1. 'A'가 없어서 그냥 차례대로 누르면 되는 경우
    if 0 not in num_list:
        return sum(num_list) + len(num_list) - 1
    
    arr = []
    # 'A'가 아닌 원소의 인덱스 리스트를 추출
    for idx, val in enumerate(num_list):
        if val == 0:
            continue
        else:
            arr.append((idx, val))
    
    # case 2. 다 'A'인 경우
    if not arr:
        return 0

    # case 3. 일반 경우
    # 1) 오른쪽으로 갔다가 왼쪽으로 가는 경우 => a[0] * 2 + (len(name) - b[0])
    # 어떤 인덱스(i)까지 갔다가 다시 돌아온 후 끝에서부터 그 다음 인덱스(i+1)까지 뒤로 돌아와야함 
    # 2) 왼쪽으로 갔다가 오른쪽으로 가는 경우 => (len(name) - b[0]) * 2 + a[0]  
    # i + 1까지 거꾸로 왔다가 다시 끝까지가고, 처음부터 i로 가는 방법
    for a, b in zip(arr[:-1], arr[1:]):
        move_cnt = min(a[0] * 2 + (len(name) - b[0]), a[0] + (len(name) - b[0]) * 2 ) 
        answer = min(answer, move_cnt)
    # 3) 오른쪽으로 가는 경우 => arr[-1][0]
    # 4) 왼쪽으로 가는 경우 => len(num_list) - arr[0][0]
    answer = min(len(num_list) - arr[0][0], arr[-1][0], answer)    
    answer += sum(num_list)
    return answer


# 테스트 케이스
print(solution("JAN")) # 23
print(solution("AAA")) # 0
print(solution("JEROEN")) # 56
print(solution("AAABBBABA")) # 10
print(solution("AAB"))  # 2   => 20(23, 25?)번대 테스트케이스
print(solution("AAAAABBAAAAAAABAAA"))  # 16
print(solution("AAAAAAAAJAAAA"))  # 14
print(solution("AAAAAABBB"))  # 6  => 12, 15번 테스트케이스 (뭉탱이로 문자가 있을때)
print(solution("BBABAAAB"))  # 9
