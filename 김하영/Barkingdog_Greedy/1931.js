const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = Number(input.shift());
const meetings = input
  .map((str) => str.split(" ").map(Number))
  .sort((a, b) => {
    if (a[1] - b[1] === 0) {
      return a[0] - b[0];
    }
    return a[1] - b[1];
  });

const solution = () => {
  let result = 1;
  let last = 0;
  last = meetings[0][1];
  for (let i = 1; i < meetings.length; i++) {
    if (last <= meetings[i][0]) {
      result++;
      last = meetings[i][1];
    }
  }

  return result;
};

console.log(solution());
