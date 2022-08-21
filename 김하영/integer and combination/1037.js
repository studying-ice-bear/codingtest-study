const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "김하영/input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

input.shift();

const nums = input[0].split(" ").map(Number);

const solution = (nums) => {
  const max = Math.max(...nums);
  const min = Math.min(...nums);

  return max * min;
};

console.log(solution(nums));
