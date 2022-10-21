const fs = require("fs");

const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];

const arr = input[1].split(" ").map((v) => +v);
const x = +input[2];

const twoPointer = (arr, x) => {
  arr.sort((a, b) => a - b);
  let answer = 0;
  let start = 0;
  let end = arr.length - 1;

  while (start < end) {
    if (arr[start] + arr[end] === x) {
      answer++;
      start++;
    } else if (arr[start] + arr[end] > x) {
      end--;
    } else {
      start++;
    }
  }

  return answer;
};

console.log(twoPointer(arr, x));
