import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
avg = round(sum(nums) / N)
sys.stdout.write(str(avg) + '\n')

# 자리수 조절
# 1. 반올림 round(number[, ndigits])
# Doc: https://docs.python.org/3/library/functions.html?highlight=round#round
# ndigits 값이 없으면 정수와 가깝게 계산하여 반환
# 2. 올림 math.ceil()
# Doc: https://docs.python.org/3/library/math.html?highlight=math%20ceil#math.ceil
# 3. 내림 math.floor()
# Doc: https://docs.python.org/3/library/math.html?highlight=math%20floor#math.floor
# 4. 버림 math.trunc()
# Doc: https://docs.python.org/3/library/math.html?highlight=trunc#math.trunc

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# N이 짝수인 경우 두 수의 평균으로 결정
nums.sort()

median_idx = len(nums) // 2
median = round((nums[median_idx] + nums[median_idx - 1]) / 2) if len(nums) % 2 == 0 else nums[median_idx]
sys.stdout.write(str(median) + '\n')

# 파이썬에서 나눗셈
# /: float형 나눗셈
# //: 나눗셈의 몫
# %: 나눗셈의 나머지
# divmod(): 나눗셈의 몫과 나머지를 튜플형식으로 반환

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# Doc: https://docs.python.org/3/library/stdtypes.html#lists
# 시도
# freq = [0] * 8001
# for num in nums:
#     freq[num] += 1
#
# max_freq_idx1 = freq.index(max(freq)) if freq.index(max(freq)) <= 4000 else freq.index(max(freq)) - 8001
# max_freq_value1 = freq[max_freq_idx1]
#
# freq[max_freq_idx1] = 0
#
# max_freq_idx2 = freq.index(max(freq)) if freq.index(max(freq)) <= 4000 else freq.index(max(freq)) - 8001
# max_freq_value2 = freq[max_freq_idx2]
#
# max_freq_idx = max_freq_idx1
# if max_freq_value1 == max_freq_value2:
#     max_freq_idx = max_freq_idx2
# 테스트 케이스
# 3
# -1000
# -4000
# 4000
# 결과값
# -333
# -1000
# -4000 # -1000을 빼질 않는다. max 함수가 순서대로 뽑는데, 나는 자료구조를 0...4000, -4000...-1 로 해놨기 때문에 의도한 대로 작동하지 않는다.
# 8000

# dict로 해보면 될거 같은데...
# Doc: https://docs.python.org/3/library/stdtypes.html#dict
# 검색결과, Counter 라는 라이브러리가 있다고 한다.
freq_num = 0

freq = Counter(nums).most_common(2) # -4000, -1000, 4000 입력시 [(-4000, 1), (-1000, 1)] 반환

if len(nums) > 1:
    if freq[0][1] == freq[1][1]:
        freq_num = freq[1][0]
    else:
        freq_num = freq[0][0]
else:
    freq_num = freq[0][0]

sys.stdout.write(str(freq_num) + '\n')

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
max = nums[len(nums) - 1]
min = nums[0]
diff = max - min
sys.stdout.write(str(diff) + '\n')