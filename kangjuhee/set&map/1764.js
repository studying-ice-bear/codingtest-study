// 듣보잡

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = input
  .shift()
  .split(" ")
  .map((i) => +i);

const listenArr = input.slice(0, N).map((i) => i.trimEnd());
const watchArr = new Set(input.slice(N).map((i) => i.trimEnd()));
let result = [];
for (let i = 0; i < N; i++) {
  if (watchArr.has(listenArr[i])) result.push(listenArr[i]);
}

result.sort((a, b) => a.localeCompare(b));

console.log(result.length);
console.log(result.join("\n"));
