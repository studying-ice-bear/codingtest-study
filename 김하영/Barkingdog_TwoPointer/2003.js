const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input
  .shift()
  .split(" ")
  .map((str) => Number(str.trim()));
const inputArr = input[0].split(" ").map((str) => Number(str.trim()));

const solution = (inputArr) => {
  let first = 0;
  let last = 0;
  let count = 0;

  while (first < inputArr.length && last < inputArr.length) {
    const sum = inputArr
      .slice(first, last + 1)
      .reduce((acc, cur) => acc + cur, 0);

    if (sum < M) {
      last++;
    } else if (sum > M) {
      first++;
    } else {
      count++;
      first++;
    }
  }

  return count;
};

console.log(solution(inputArr));
