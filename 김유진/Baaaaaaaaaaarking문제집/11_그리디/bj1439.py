import sys
arr = list(int(a) for a in sys.stdin.readline().strip())

zero = one = 0

if arr[0] == 0:
    zero += 1
else:
    one += 1

for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
        if arr[i] == 0:
            zero += 1
        else:
            one += 1

print(min(zero, one))


'''
문제 링크: https://www.acmicpc.net/problem/1439
    다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 
    다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 
    뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

문제 아이디어 1:
연속으로 0 또는 1로 이루어진 그룹 만들기
0 그룹의 개수, 1그룹의 개수 비교

문제 아이디어 2★:
바뀌는 시점에서 각각 0으로 바뀌는지 1로 바뀌는지 count
'''