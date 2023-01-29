const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = Number(input.shift());
const numbers = input.map(Number).sort((a, b) => a - b);

const solution = () => {
  let result = numbers[0] * N;
  for (let i = 1; i < numbers.length; i++) {
    result = Math.max(result, numbers[i] * (N - i));
  }

  return result;
};

console.log(solution());
