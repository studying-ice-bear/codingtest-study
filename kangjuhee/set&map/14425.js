// 문자열 집합

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = input
  .shift()
  .split(" ")
  .map((i) => +i);

const set = new Set(input.slice(0, N).map((i) => i.trimEnd()));
const arr = input.slice(N).map((i) => i.trimEnd());

let result = 0;
for (let i = 0; i < arr.length; i++) {
  if (set.has(arr[i])) result += 1;
}

console.log(result);
