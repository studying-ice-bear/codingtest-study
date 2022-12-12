const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((v) => +v);
const numArray = input.slice(1);
const dp = Array.from({ length: 1000001 }, () => 0);
dp[1] = 1;
dp[2] = 2;
dp[3] = 4;

const representaionAsSum = (num) => {
  for (let i = 4; i <= num; i++) {
    dp[i] = dp[i - 2] + dp[i - 3] + dp[i - 1];
  }

  return dp[num];
};

const solution = (numArray) => {
  const result = numArray.map(representaionAsSum);

  console.log(result.join("\n"));
};

solution(numArray);
