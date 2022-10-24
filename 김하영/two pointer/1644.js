const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = +input[0];

const solution = (N) => {
  // 에라토스테네스의 체

  const arr = new Array(N + 1).fill(true);
  arr[0] = false;
  arr[1] = false;
  for (let i = 2; i <= N; i++) {
    if (arr[i]) {
      for (let j = i * i; j <= N; j += i) {
        arr[j] = false;
      }
    }
  }

  const nums = [];

  for (let i = 0; i <= N; i++) {
    if (arr[i]) {
      nums.push(i);
    }
  }

  let start = 0;
  let end = 0;
  let answer = 0;
  let sum = 0;

  for (start; start < N; start++) {
    while (sum < N && end < nums.length) {
      sum += nums[end++];
    }
    if (sum === N) {
      answer++;
    }
    sum -= nums[start];
  }

  return answer;
};

console.log(solution(N));
