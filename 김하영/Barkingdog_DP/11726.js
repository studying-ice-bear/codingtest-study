const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((v) => +v)[0];

const dp = Array.from({ length: 1000001 }, () => 0);
dp[1] = 1;
dp[2] = 2;
const mod = 10007;

const solution = () => {
  for (let i = 3; i <= input; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod;
  }

  return dp[input];
};

console.log(solution());
