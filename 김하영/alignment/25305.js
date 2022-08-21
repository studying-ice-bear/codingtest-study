const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().split("\n");

const N = Number(input[0].split(" ")[0]);
const K = Number(input[0].split(" ")[1]);
const arr = input[1].split(" ").map((item) => Number(item));

const solution = (arr) => {
  const sorted = arr.sort((a, b) => b - a);

  return sorted.splice(0, K).at(-1);
};

console.log(solution(arr));
