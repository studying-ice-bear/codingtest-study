const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input
  .shift()
  .split(" ")
  .map((str) => Number(str.trim()));
const inputArr = input.map((str) => Number(str.trim())).sort((a, b) => a - b);

const solution = (inputArr) => {
  let first = 0;
  let last = 1;

  let min = Infinity;

  while (first < inputArr.length && last < inputArr.length) {
    const diff = inputArr[last] - inputArr[first];

    if (diff < M) {
      last++;
    } else {
      min = Math.min(min, diff);
      first++;
    }
  }

  return min;
};

console.log(solution(inputArr));
