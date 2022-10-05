//백준 2293번 동전 1

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const [NK, ...temp] = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, k] = NK.split(" ").map(Number);
const coins = temp.map(Number);

const solution = (n, k, coins) => {
  let dp = Array.from({ length: k + 1 }, () => 0);
  dp[0] = 1;
  for (let i = 0; i < n; i++) {
    // 코인의 갯수만큼 반복
    for (let j = coins[i]; j <= k; j++) {
      // 코인의 가치부터 k까지 반복
      dp[j] += dp[j - coins[i]];
    }
  }
  return dp[k];
};

console.log(solution(n, k, coins));

// 1과 2 코인으로 합 4을 구한다고 했을 때
// (2, 2) (2, 1, 1)은 앞의 2를 빼고 본다면
// (0, 2) = 2코인으로 합 2를 구할 때, (0, 1, 1) = 1코인으로 합 2를 구할 때 총 2가지 경우의 수가 있다.

// 1과 2와 5 코인으로 10의 합을 구한다고 했을 때
// 5 = 1과 2코인으로 5를 구하는 경우의 수 + 5코인 하나
// 6 = 1과 2코인으로 6를 구하는 경우의 수 + (5코인 하나 + 합 1을 구하는 경우의 수)
// 7 = 1과 2코인으로 7를 구하는 경우의 수 + (5코인 하나 + 합 2를 구하는 경우의 수)
// 8 = 1과 2코인으로 8를 구하는 경우의 수 + (5코인 하나 + 합 3을 구하는 경우의 수)
// 9 = 1과 2코인으로 9를 구하는 경우의 수 + (5코인 하나 + 합 4를 구하는 경우의 수)
// 10 = 1과 2코인으로 10를 구하는 경우의 수 + (5코인 하나 + 합 5를 구하는 경우의 수)
