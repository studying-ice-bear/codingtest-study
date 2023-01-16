const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = input.shift();
const numArray = input.map((v) => v.split(" ").map(Number));
const dp = Array.from(new Array(1005), () => new Array(3).fill(0));
const R = Array.from({ length: 1005 }, () => 0);
const G = Array.from({ length: 1005 }, () => 0);
const B = Array.from({ length: 1005 }, () => 0);

const solution = (numArray) => {
  for (let i = 0; i < N; i++) {
    R[i] = numArray[i][0];
    G[i] = numArray[i][1];
    B[i] = numArray[i][2];
  }

  dp[0][0] = R[0];
  dp[0][1] = G[0];
  dp[0][2] = B[0];

  for (let i = 1; i < N; i++) {
    dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + R[i];
    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + G[i];
    dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + B[i];
  }

  return Math.min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]);
};

console.log(solution(numArray));
