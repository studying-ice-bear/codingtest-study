// 프로그래머스 사칙연산

const solution = (arr) => {
  const nums = [];
  const operations = [];
  let answer = 0;

  for (let i = 0; i < arr.length; i++) {
    if (i % 2 === 0) {
      nums.push(Number(arr[i]));
    } else {
      operations.push(arr[i]);
    }
  }

  const dp = Array.from(Array(nums.length), () => Array(nums.length).fill(0));
  const minDp = Array.from(Array(nums.length), () =>
    Array(nums.length).fill(0)
  );
  const maxDp = Array.from(Array(nums.length), () =>
    Array(nums.length).fill(0)
  );

  for (let i = 0; i < nums.length; i++) {
    dp[i][i] = nums[i];
    minDp[i][i] = nums[i];
    maxDp[i][i] = nums[i];
  }

  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < nums.length - i; j++) {
      const k = j + i;
      const [min, max] = getMinMax(j, k, operations, minDp, maxDp);
      minDp[j][k] = min;
      maxDp[j][k] = max;
    }
  }

  answer = maxDp[0][nums.length - 1];

  return answer;
};

// 테스트
console.log(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])); // 3
