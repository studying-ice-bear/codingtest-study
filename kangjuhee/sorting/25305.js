// 커트라인

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
let num = input.shift();
num = num.split(" ").map((i) => Number(i)); // 숫자를 배열로 바꾼다. [5, 2]
input = input[0].split(" ").map((i) => Number(i));
input = input.sort((a, b) => b - a);
console.log(input[num[1] - 1]);
