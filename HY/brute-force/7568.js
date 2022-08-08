const fs = require("fs");

const filePath =
  process.platform === "linux" ? "/dev/stdin" : "brute-force/input.txt";

let input = fs
  .readFileSync("brute-force/input.txt")
  .toString()
  .split("\n")
  .map((item) => item.split(" "));
const N = input.shift();

const kgArr = input.map((item) => Number(item[0]));
const cmArr = input.map((item) => Number(item[1]));
const result = [];

for (let i = 0; i < N; i++) {
  let count = 0;
  for (let j = 0; j < N; j++) {
    if (kgArr[i] < kgArr[j] && cmArr[i] < cmArr[j]) {
      count++;
    }
  }
  result.push(count + 1);
}

console.log(result.join(" "));
