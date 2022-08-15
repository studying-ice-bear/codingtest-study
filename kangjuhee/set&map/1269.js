// 대칭 차집합

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
const a = input
  .shift()
  .split(" ")
  .map((i) => +i);
const b = input
  .shift()
  .split(" ")
  .map((i) => +i);

const setA = new Set(a);
const setB = new Set(b);
let result = 0;

for (let i = 0; i < a.length; i++) {
  if (!setB.has(a[i])) result += 1;
}

for (let i = 0; i < b.length; i++) {
  if (!setA.has(b[i])) result += 1;
}

console.log(result);
