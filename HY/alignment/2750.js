const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((num) => parseInt(num));

const N = Number(input.shift());
const solution = (input) => {
  const sortedArr = input.sort((a, b) => a - b);

  return (result = sortedArr.join("\n"));
};

console.log(solution(input));

// 2751도 가능함
