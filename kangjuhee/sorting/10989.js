// 수 정렬하기 3 => js로 풀 수 없는 문제

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
let result = "";
input.shift();
input = input.map((i) => Number(i.trim()));
input = input.sort((a, b) => a - b);
input.forEach((el) => {
  result += `${el}\n`;
});
console.log(result.trimEnd());
