const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = Number(input[0]);
const A = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => {
    return a - b;
  });
const B = input[2]
  .split(" ")
  .map(Number)
  .sort((a, b) => {
    return b - a;
  });

const solution = () => {
  let result = 0;
  for (let i = 0; i < N; i++) {
    result += A[i] * B[i];
  }
  return result;
};

console.log(solution());
