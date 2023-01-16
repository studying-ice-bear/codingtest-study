const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, S] = input[0].split(" ").map(Number);
const numbers = input[1].split(" ").map(Number);

let result = 0;

const solution = (idx, sum) => {
  if (idx === N) {
    if (sum === S) result++;
    return;
  }

  solution(idx + 1, sum + numbers[idx]);
  solution(idx + 1, sum);
};

solution(0, 0);

console.log(S === 0 ? result - 1 : result);
