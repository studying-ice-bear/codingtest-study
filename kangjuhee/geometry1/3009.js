// 네 번째 점

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" ").map((j) => +j));

let x4 = [];
let y4 = [];
let result = [];
for (let i = 0; i < input.length; i++) {
  let [x, y] = input[i];
  x4.push(x);
  y4.push(y);
}

x4 = x4.sort((a, b) => a - b);
y4 = y4.sort((a, b) => a - b);

x4[0] === x4[1] ? result.push(x4[2]) : result.push(x4[0]);
y4[0] === y4[1] ? result.push(y4[2]) : result.push(y4[0]);

console.log(result.join(" "));
