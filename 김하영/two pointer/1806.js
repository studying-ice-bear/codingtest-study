const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, S] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map((v) => +v);

const solution = (N, S, arr) => {
  let start = 0;
  let end = 0;
  let answer = Infinity;
  let sum = 0;

  for (start; start < N; start++) {
    // 합구하기
    while (sum < S && end < N) {
      sum += arr[end++];
    }
    if (sum >= S) {
      answer = Math.min(answer, end - start);
    }
    sum -= arr[start];
  }

  return answer === Infinity ? 0 : answer;
};

console.log(solution(N, S, arr));
