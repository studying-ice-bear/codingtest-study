// 숫자 카드 2

let input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");

const cardArr = input[1].split(" ").map((i) => +i);
const findArr = input[3].split(" ").map((i) => +i);
const dict = new Map();
for (let i = 0; i < findArr.length; i++) {
  dict.set(findArr[i], 0);
}

for (let i = 0; i < cardArr.length; i++) {
  if (dict.has(cardArr[i])) dict.set(cardArr[i], dict.get(cardArr[i]) + 1);
}

let result = [];
for (let i = 0; i < findArr.length; i++) {
  result.push(dict.get(findArr[i]));
}
console.log(result.join(" "));
