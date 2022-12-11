const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = Number(input[0]);
const times = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const solution = () => {
  let result = 0;
  const arr = [];
  times.forEach((time) => {
    result += time;
    arr.push(result);
  });

  return arr.reduce((prev, curr) => {
    return prev + curr;
  }, 0);
};

console.log(solution());
