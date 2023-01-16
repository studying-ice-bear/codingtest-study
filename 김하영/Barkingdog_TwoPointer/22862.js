const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input
  .shift()
  .split(" ")
  .map((str) => Number(str.trim()));
const inputArr = input[0].split(" ").map((str) => Number(str.trim()));

const solution = (inputArr) => {
  let left = 0;
  let right = 0;
  let count = 0;

  while (right < inputArr.length) {
    if (inputArr[right] % 2 === 0) {
      count++;
    }
    while (count > K) {
      if (inputArr[left] % 2 === 0) {
        count--;
      }
      left++;
    }
    right++;
  }

  return count <= K ? right - left - count + 1 : count;
};

console.log(solution(inputArr));
