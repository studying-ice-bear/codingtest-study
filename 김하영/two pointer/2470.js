const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];
const nums = input[1].split(" ").map(Number);

const solution = (n, nums) => {
  nums.sort((a, b) => a - b);
  let start = 0;
  let end = n - 1;
  let sum = Infinity;
  let a = 0;
  let b = 0;
  let temp = Infinity;

  while (start < end) {
    sum = nums[start] + nums[end];
    if (sum < 0) {
      if (Math.abs(sum) < Math.abs(temp)) {
        temp = sum;
        a = nums[start];
        b = nums[end];
      }
      start++;
    } else {
      if (Math.abs(sum) < Math.abs(temp)) {
        temp = sum;
        a = nums[start];
        b = nums[end];
      }
      end--;
    }
  }

  if (nums.indexOf(a) > nums.indexOf(b)) {
    return `${b} ${a}`;
  } else {
    return `${a} ${b}`;
  }
};
console.log(solution(n, nums));
