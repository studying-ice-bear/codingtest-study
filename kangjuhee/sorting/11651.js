// 좌표 정렬하기 2

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");

input.shift();

input = input.map((i) => i.split(" ").map((i) => Number(i)));
input = input.sort((a, b) => a[0] - b[0]);
input = input.sort((a, b) => a[1] - b[1]);

// for (let i = 0; i < input.length; i++) {
//   console.log(input[i].join(" "));
// }

let result = "";
input.forEach((el) => {
  result += `${el[0]} ${el[1]}\n`;
});
console.log(result.trimEnd());
