const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const [x, y, w, h] = input;

const solution = (x, y, w, h) => {
  const w1 = w - x;
  const w2 = -(0 - x);
  const h1 = h - y;
  const h2 = -(0 - y);
  const arr = [w1, w2, h1, h2];

  const min = Math.min(...arr);
  return min;
};

console.log(solution(x, y, w, h));
