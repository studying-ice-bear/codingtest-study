// 백준 10942번 문제 팰린드롬?

const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = +input[0];
const arr = input[1].split(" ").map((v) => +v);
const M = +input[2];
const testCase = input.slice(3).map((v) => v.split(" ").map((v) => +v));

const solution = (N, arr, M, testCase) => {
  let answer = "";

  const dp = Array.from(Array(N), () => Array(N).fill(0));

  for (let i = 0; i < N; i++) {
    dp[i][i] = 1;
    if (arr[i] === arr[i + 1]) {
      dp[i][i + 1] = 1;
    }
  }

  for (let i = 2; i < N; i++) {
    for (let j = 0; j < N - i; j++) {
      if (arr[j] === arr[j + i] && dp[j + 1][j + i - 1] === 1) {
        dp[j][j + i] = 1;
      }
    }
  }

  for (let i = 0; i < M; i++) {
    const [start, end] = testCase[i];
    answer += dp[start - 1][end - 1] + "\n";
  }

  return answer;
};

console.log(solution(N, arr, M, testCase));
