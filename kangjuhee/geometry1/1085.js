// 직사각형에서 탈출

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split(" ")
  .map((i) => +i);

const [x, y, w, h] = input;

console.log(Math.min(x, w - x, y, h - y));
