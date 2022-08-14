import sys
f = sys.stdin.readline

n = int(f())
num = 666
cnt = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1
    
    
"""
풀이
666부터 1씩 증가시켜 더한 값에 666이 존재하면 count += 1 해주면서 n과 같으면 count 출력
"""