//백준 11066

const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const [T, ...input] = fs
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

const solution = (T, input) => {
  let answer = "";
  for (let i = 0; i < T; i++) {
    let K = input[i * 2];
    let arr = input[i * 2 + 1];

    let sum = Array.from(Array(K), () => Array(K).fill(0));
    let dp = Array.from(Array(K), () => Array(K).fill(0));

    for (let i = 0; i < K; i++) {
      for (let j = i; j < K; j++) {
        if (i === j) {
          sum[i][j] = arr[i];
        } else {
          sum[i][j] = sum[i][j - 1] + arr[j];
        }
      }
    }

    for (let i = 1; i < K; i++) {
      for (let j = 0; j < K - i; j++) {
        dp[j][j + i] = Number.MAX_SAFE_INTEGER;
        for (let k = j; k < j + i; k++) {
          dp[j][j + i] = Math.min(
            dp[j][j + i],
            dp[j][k] + dp[k + 1][j + i] + sum[j][j + i]
          );
        }
      }
    }
    answer += dp[0][K - 1] + "\n";
  }
  console.log(answer);

  return answer;
};

console.log(solution(T, input));
