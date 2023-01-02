// 백준 11049번 행렬 곱셈 순서

const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const [N, ...input] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((v) => {
    if (v.split(" ").length > 1) {
      return v.split(" ").map((v) => +v);
    } else {
      return +v;
    }
  });

const solution = (N, input) => {
  let answer = 0;
  let dp = Array.from(Array(N), () => Array(N).fill(0));
  let arr = Array.from(Array(N), () => Array(2).fill(0));

  for (let i = 0; i < N; i++) {
    arr[i][0] = input[i][0];
    arr[i][1] = input[i][1];
  }

  for (let i = 1; i < N; i++) {
    for (let j = 0; j < N - i; j++) {
      dp[j][j + i] = Number.MAX_SAFE_INTEGER;
      for (let k = j; k < j + i; k++) {
        dp[j][j + i] = Math.min(
          dp[j][j + i],
          dp[j][k] + dp[k + 1][j + i] + arr[j][0] * arr[k][1] * arr[j + i][1]
        );
        console.log(dp);
      }
    }
  }

  answer = dp[0][N - 1];
  return answer;
};

console.log(solution(N, input));

// 설명
// 1. dp[i][j] = i번째 행렬부터 j번째 행렬까지 곱하는데 필요한 최소 연산 횟수
// 2. dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1]) (i <= k < j)
// 3. dp[i][i] = 0
// 4. dp[i][i+1] = arr[i][0] * arr[i][1] * arr[i+1][1]
