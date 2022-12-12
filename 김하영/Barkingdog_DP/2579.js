const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const stairs = input.slice(1).map((v) => +v);

const dp = Array.from(Array(301), () => Array(2).fill(0)); // 0 = 현재까지 한 계단, 1 = 현재까지 두 계단
dp[1][0] = stairs[0];
dp[2][0] = stairs[1];
dp[2][1] = stairs[0] + stairs[1];

const solution = (stairs) => {
  for (let i = 3; i <= stairs.length; i++) {
    dp[i][0] = Math.max(dp[i - 2][0], dp[i - 2][1]) + stairs[i - 1];
    dp[i][1] = dp[i - 1][0] + stairs[i - 1];
  }
  return Math.max(dp[stairs.length][0], dp[stairs.length][1]);
};

console.log(solution(stairs));
