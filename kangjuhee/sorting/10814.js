// 나이순 정렬

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
input.shift();
input = input
  .map((i) => i.split(" "))
  .map((i) => [Number(i[0]), i[1].trimEnd()])
  .sort((a, b) => a[0] - b[0]);

let result = "";
input.forEach((el) => {
  result += `${el[0]} ${el[1]}\n`;
});
console.log(result.trimEnd());
