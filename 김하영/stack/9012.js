const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = input.shift();
const inputArr = input.map((str) => str.trim().split(""));

const isVPS = (arr) => {
  let sum = 0;

  for (const str of arr) {
    const num = str === "(" ? 1 : -1;
    sum += num;
    if (sum < 0) {
      return "NO";
    }
  }
  return sum === 0 ? "YES" : "NO";
};

const solution = (inputArr) => {
  const result = [];

  for (const arr of inputArr) {
    const VPS = isVPS(arr);

    result.push(VPS);
  }

  return result.join("\n");
};

console.log(solution(inputArr));
